let _ = require("underscore");


let cakeTypes = [
  {weight: 7, value: 160},
  {weight: 3, value: 90},
  {weight: 2, value: 15},
];

const capacity = 20;


//return the maximum monetary value up to max capacity.

function maxDuffelBagValue (cakeTypes, capacity) {
  let i = 0
  let j = 0
  let firstCake;
  let nthCake;
  let currentValue;
  let bagCombos= []

  while (i < cakeTypes.length) {
    firstCake = cakeTypes[i]
    let currentWeight = firstCake.weight
    let currentValue  = firstCake.value
    while (j < cakeTypes.length) {
      nthCake = cakeTypes[j]

      let prospectiveWeight = currentWeight + nthCake.weight
      if (prospectiveWeight <= capacity) {
        currentWeight = prospectiveWeight
        currentValue += nthCake.value
      }

      if (prospectiveWeight >= capacity) {
        bagCombos.push({weight: currentWeight, value: currentValue})
        currentWeight = firstCake.weight
        currentValue = firstCake.value
        j++
      }
    }
    i++
  }

  console.log('==> bagCombos', bagCombos);
  return _.max(bagCombos, (e) => {return e.value})
}

let result = maxDuffelBagValue(cakeTypes, capacity);

