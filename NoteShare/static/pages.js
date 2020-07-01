let next = document.getElementById('next_button');
let prev = document.getElementById('prev_button');

let counter = 1;
let n = 10; //n is the number of entries per page
let total = 1;

while(document.getElementById(String(total)) != null)
{
	total++;
}
total--;

console.log(total);

let j = 1;

while(j <= total)
{
	if(j<=n)
	{
		document.getElementById(String(j)).style.display="table-row";
	}
	else
	{
		document.getElementById(String(j)).style.display="none";
	}
	j++;
}

prev.onclick = function() {
	if(counter > 1)
	{
		counter--;
	}

	let i = 1;

	while(i <= total)
	{
		if(i <= counter*n && i > (counter-1)*n)
		{
			document.getElementById(String(i)).style.display="table-row";
		}
		else
		{
			document.getElementById(String(i)).style.display="none";
		}
		i++;
	}
}

next.onclick = function() {
	if(counter*n < total)
	{
		counter++;
	}

	let i = 1;

	while(i <= total)
	{
		if(i <= counter*n && i > (counter-1)*n)
		{
			document.getElementById(String(i)).style.display="table-row";
		}
		else
		{
			document.getElementById(String(i)).style.display="none";
		}
		i++;
	}
}
