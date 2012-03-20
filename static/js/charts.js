//here you place the ids of every element you want.
var chart=new Array('chart1','chart2','chart3');

function Switchid(id){	
	Hideallids();
	Showdiv(id);
}

function Hideallids(){
	//loop through the array and hide each element by id
	for (var i=0;i<chart.length;i++){
		Hidediv(chart[i]);
	}		  
}

function Hidediv(id) {
	//safe function to hide an element with a specified id
	if (document.getElementById) { // DOM3 = IE5, NS6
		document.getElementById(id).style.display = 'none';
	}
	else {
		if (document.layers) { // Netscape 4
			document.id.display = 'none';
		}
		else { // IE 4
			document.all.id.style.display = 'none';
		}
	}
}

function Showdiv(id) {
	//safe function to show an element with a specified id
		  
	if (document.getElementById) { // DOM3 = IE5, NS6
		document.getElementById(id).style.display = 'block';
	}
	else {
		if (document.layers) { // Netscape 4
			document.id.display = 'block';
		}
		else { // IE 4
			document.all.id.style.display = 'block';
		}
	}
}

