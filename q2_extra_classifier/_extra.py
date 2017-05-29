from q2_feature_classifier.classifier import _register_fitter

nb_extra = [['feat_ext',
             {'__type__': 'custom.ChunkedHashingVectorizer',
              'analyzer': 'char',
              'norm': None,
              'non_negative': True}],
            ['norm',
             {'__type__': 'feature_extraction.text.TfidfTransformer'}],
            ['classify',
             {'__type__': 'custom.LowMemoryMultinomialNB',
              'fit_prior': False}]]

_register_fitter('nb_extra', nb_extra)
