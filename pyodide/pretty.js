function pretty(obj) {
	if (typeof(obj) == "string") {
		return `'${obj}'`
	} else if (Array.isArray(obj) || 
		obj.__proto__.constructor.__proto__.name == 'TypedArray') {
		var mapped = obj.map(pretty);
		return `[${mapped}]`
	} else if (typeof(obj) == "object") {
		var members = []
		for (k in obj) {
			members.push([pretty(k), pretty(obj[k])].join(": "))
		}
		return `{${members}}`
	} else {
		let v = obj.toString()
		return (v) ? v : `${obj}`
	}
}
