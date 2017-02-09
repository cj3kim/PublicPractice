
function quick_sort(ary) {
  if (ary.length === 0) { return ary; }
  if (ary.length === 1) { return ary; }

  if (ary.length === 2) {
    if (ary[0] > ary[1]) {
      return [ary[1], ary[0]]
    } else {
      return ary
    }
  }

  var pivotIndex = Math.floor(ary.length/2);
  var pivotNumber = ary[pivotIndex];

  var leftAry  = [];
  var rightAry = [];

  ary.forEach(function (n, i) {
    if ( i === pivotIndex) {
    } else if (n <= pivotNumber) {
      leftAry.push(n)
    } else if (n > pivotNumber) {
      rightAry.push(n)
    }
  })

  var leftResult  = quick_sort(leftAry);
  var rightResult = quick_sort(rightAry);
  var result = leftResult.concat(pivotNumber,rightResult)
  console.log('==> result', result);
  return result


}

module.exports = quick_sort
