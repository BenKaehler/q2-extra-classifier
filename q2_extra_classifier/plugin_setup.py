from qiime2.plugin import Plugin

import q2_extra_classifier


plugin = Plugin(
    name='extra-classifier',
    version=q2_extra_classifier.__version__,
    website='https://github.com/benkaehler/q2-extra-classifier',
    package='q2_extra_classifier'
)
