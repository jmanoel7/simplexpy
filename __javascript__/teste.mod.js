	(function () {
		var math = {};
		var __name__ = '__main__';
		__nest__ (math, '', __init__ (__world__.math));
		var GfxDriver = __init__ (__world__.PyPlotter).tkGfx;
		var Graph = __init__ (__world__.PyPlotter).Graph;
		var Gfx = __init__ (__world__.PyPlotter).Gfx;
		var gfx = GfxDriver.Window (__kwargtrans__ ({title: 'Function Plotter'}));
		var gr = Graph.Cartesian (gfx, -(4.0), -(2.0), 4.0, 2.0);
		gr.addPen ('sin(x)', Gfx.RED_PEN);
		var __iterable0__ = gr.xaxisSteps (-(4.0), 4.0);
		for (var __index0__ = 0; __index0__ < len (__iterable0__); __index0__++) {
			var x = __iterable0__ [__index0__];
			gr.addValue ('sin(x)', x, math.sin (x));
		}
		gfx.waitUntilClosed ();
		__pragma__ ('<use>' +
			'PyPlotter' +
			'math' +
		'</use>')
		__pragma__ ('<all>')
			__all__.Gfx = Gfx;
			__all__.GfxDriver = GfxDriver;
			__all__.Graph = Graph;
			__all__.__name__ = __name__;
			__all__.gfx = gfx;
			__all__.gr = gr;
			__all__.x = x;
		__pragma__ ('</all>')
	}) ();
