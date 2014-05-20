class UnknownUnit

    def initialize(node)
      @node = node
    end

    def type
      'UnknownUnit'
    end

    def to_json
      as_json
    end

    def as_json
      {
          Unit: 'Unkown'
      }
    end
end