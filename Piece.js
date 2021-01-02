class Piece {
	constructor(s) {
		if (s === 'X') this.value = 1;
		else if (s === 'O') this.value = -1;
		else if (s === ' ') this.value = 0;
	}
	
	getValue() {
		return this.value;
	}

	setValue(s) {
		if (s === 'X') this.value = 1;
		else if (s === 'O') this.value = -1;
		else if (s === ' ') this.value = 0;
	}

	toString() {
		if this.value == 1 return '[X]'
		else if this.value == -1 return '[O]'
		else if this.value == 0 return '[ ]'
	}
}
