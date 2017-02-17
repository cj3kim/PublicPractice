class Node {
  constructor (props) {
    let {nodeValue} = props
    this.nodeValue = nodeValue
    this.left = null;
    this.right = null;
  }

  addNumber (number) {
    if (isNaN(this.nodeValue)) {
      this.nodeValue = number
    } else {
      let key = number <= this.nodeValue ? "left" : "right"
      if (this[key]) {
        this[key].addNumber(number)
      } else {
        this[key] = new Node({"nodeValue": number})
      }
    }
  }

  returnTree (node, number) {
    if (number === node.nodeValue) {
      return node
    }
    let key = number <= node.nodeValue ? "left" : "right"
    return node.returnTree(node[key], number)
  }
}


let initial_numbers = [1,2,3,4,5,6]
let initialNode = new Node({})
initial_numbers.forEach((k) => { initialNode.addNumber(k) })
console.log('==> initialNode', JSON.stringify(initialNode));
console.log('==> initialNode.returnTree(4)', initialNode.returnTree(initialNode,4));




