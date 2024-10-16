{
  'targets': [
    {
      'target_name': 'cpufeatures',
      'cflags!': [ '-fno-exceptions' ],
      'cflags_cc!': [ '-fno-exceptions' ],
      'xcode_settings': { 'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
        'CLANG_CXX_LIBRARY': 'libc++',
        'MACOSX_DEPLOYMENT_TARGET': '10.7',
      },
      'msvs_settings': {
        'VCCLCompilerTool': { 'ExceptionHandling': 1 },
      },
      'dependencies': [ 'deps/cpu_features/cpu_features.gyp:cpu_features' ],
      'include_dirs': [
        '<!(node -p "require(\'node-addon-api\').include_dir")',
        'src',
      ],
      'sources': [
        'src/binding.cc'
      ],
      'cflags': [ '-O3' ],
    },
  ],
}
