var chai = require("chai")
var chaiImmutable = require("chai-immutable");
var assert = chai.assert
chai.use(chaiImmutable);

var Immutable = require("immutable");
var List = Immutable.List;
var rp = require("./recursive_permutations");

var gen_permutations = rp.gen_permutations;
var createHeaderPermutations = rp.createHeaderPermutations;

describe("#create_header_permutations", function() {

  it("should create an initial set of permutations", function () {
    var result = createHeaderPermutations(List([1,2,3]))
    var expectedResult = List([
      List([1,2,3]),
      List([2,1,3]),
      List([3,1,2]),
    ])

    assert.deepEqual(result, expectedResult)

var result = createHeaderPermutations(List([1,2]))
    var expectedResult = List([
      List([1,2]),
      List([2,1]),
    ])

    assert.deepEqual(result, expectedResult)


  });
})

describe("recursive numbers", function() {
    it("should recursively generate a permutation from a list of integers", function () {
        var input = List([1,2,3]);
        var fn = gen_permutations;
        var result = fn(input);

        var expectedResult = List([ List([1,2,3]),
                                    List([1,3,2]),
                                    List([2,1,3]),
                                    List([2,3,1]),
                                    List([3,1,2]),
                                    List([3,2,1]),
                                  ]);


        assert.deepEqual(result, expectedResult)
    });
})




