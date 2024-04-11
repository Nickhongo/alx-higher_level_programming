#!/usr/bin/node
class Rectangle {
	constructor (w, h) {
		if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
			return;
		}
		this.width = w;
		this.height = h;
	}
	print () {
		for (let i = 0; i < this.height; i++) {
			console.log('X'.repeat(this.width));
		}
	}
	rotate () {
		const temp = this.width;
		this.width = this.height;
		this.height = temp;
	}
	double () {
		this.width = 2 * this.width;
		this.height = 2 * this.height
	}
}

class Square extends Rectangle {
	constructor (size) {
		super(size, size);
	}
}

module.exports = Square;