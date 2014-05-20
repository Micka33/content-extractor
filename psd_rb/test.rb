require_relative 'ruby/panda_psd'
require 'benchmark'
require 'pp'


Benchmark.bm(10) do |x|
  x.report('PandaPsd:') {
    psd = PandaPsd.new(file:'../psds/rmn_v3.psd').parse
    psd = PandaPsd.new(file:'psds/micka.psd').parse
    pp 'infos  -> '+psd.info.join(', ')
    pp 'errors -> '+psd.errors.join(', ')
  }
end
