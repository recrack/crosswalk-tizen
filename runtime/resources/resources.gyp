{
  'targets': [
    {
      'target_name': 'xwalk_runtime_resources',
      'type': 'none',
      'rules': [
        {
          'rule_name': 'xwalk_po2mo',
          'extension': 'po',
          'outputs': [
            '<(SHARED_INTERMEDIATE_DIR)/locales/<(RULE_INPUT_ROOT)/LC_MESSAGES/xwalk.mo',
          ],
          'action': [
            'msgfmt',
            '-o',
            '<@(_outputs)',
            '<(RULE_INPUT_PATH)',
          ],
          'message': 'Generating mo file from <(RULE_INPUT_PATH)',
        },
        {
          'rule_name': 'xwalk_edc2edj',
          'extension': 'edc',
          'outputs': [
            '<(SHARED_INTERMEDIATE_DIR)/<(RULE_INPUT_ROOT).edj',
          ],
          'action': [
            'edje_cc',
            '<(RULE_INPUT_PATH)',
            '<@(_outputs)',
          ],
          'message': 'Generating edj file from <(RULE_INPUT_PATH)',
        }
      ],
      'sources': [
        'xwalk_tizen.edc',
        'locales/ar.po',
        'locales/as.po',
        'locales/bn_BD.po',
        'locales/bn.po',
        'locales/en_PH.po',
        'locales/en.po',
        'locales/en_US.po',
        'locales/es_US.po',
        'locales/fa.po',
        'locales/fr.po',
        'locales/gu.po',
        'locales/hi.po',
        'locales/id.po',
        'locales/km.po',
        'locales/kn.po',
        'locales/ko_KR.po',
        'locales/lo.po',
        'locales/ml.po',
        'locales/mr.po',
        'locales/ms.po',
        'locales/my_ZG.po',
        'locales/ne.po',
        'locales/or.po',
        'locales/pa.po',
        'locales/pt_BR.po',
        'locales/pt_PT.po',
        'locales/ru_RU.po',
        'locales/si.po',
        'locales/ta.po',
        'locales/te.po',
        'locales/th.po',
        'locales/tl.po',
        'locales/tr_TR.po',
        'locales/ur.po',
        'locales/vi.po',
        'locales/zh_CN.po',
      ],
    }, # end of target 'xwalk_runtime_resources_locales'
  ],
}