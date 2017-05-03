import shlex
import traceback

import click
import click.testing

from q2cli.__main__ import qiime


@click.command()
@click.argument('commands', type=click.File())
def qiime_kludge(commands):
    for j, command in enumerate(commands, 1):
        args = shlex.split(command)
        assert args[0] == 'qiime', 'not a qiime command'

        for i, arg in enumerate(args):
            if arg.startswith('`cat') and arg.endswith('`'):
                filename = arg.strip('`').split(' ', 1)[1]
                with open(filename) as fh:
                    args[i] = fh.read()

        args.append('--verbose')
        runner = click.testing.CliRunner()
        result = runner.invoke(qiime, args[1:], catch_exceptions=False)
        if result.output:
            print(result.output)
        if result.exit_code != 0 and result.exc_info:
            for exc in traceback.format_exception(*result.exc_info):
                print(exc)

        assert result.exit_code == 0, 'command on line ' + str(j) + \
            ' exited with code ' + str(result.exit_code)
