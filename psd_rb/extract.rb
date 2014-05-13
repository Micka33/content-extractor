require 'psd'
require 'benchmark'
require 'pp'

def parse file
  psd = PSD.new(file)
  psd.parse!

  pp psd.tree.to_hash
end


Benchmark.bm(7) do |x|
  x.report("parse:") {parse './psds/rmn_v3.psd'}
end