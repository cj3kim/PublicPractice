var Immutable = require("immutable");
var List = Immutable.List

function createHeaderPermutations (_intAry) {
  var intAry = List(_intAry);

  var headerPermutations = intAry.map(function (e,i, _ary) {
    return _ary.delete(i).unshift(e)
  })

  return headerPermutations
}

function gen_permutations(_intAry) {
  var result = _gen_permutations(_intAry).flatten(true)
  return result
}
function _gen_permutations (_intAry) {
  var intAry = List(_intAry);

  if (intAry.size === 2) {
    return List([intAry, intAry.reverse()])
  }

  var headerPermutations = createHeaderPermutations(intAry)

  return headerPermutations.map(function (e,i) {
    var first = e.first();
    var rest  = e.rest();

    var k = _gen_permutations(rest);
    if (k.size > 2) { k = k.flatten(true) }
    var permutations = k.map(function (e) { return e.unshift(first) });
    return permutations;
  })
}

module.exports =  {
  gen_permutations: gen_permutations,
  createHeaderPermutations: createHeaderPermutations
}

