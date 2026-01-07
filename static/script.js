const display = document.getElementById("display");
const mini = document.getElementById("mini-calc");
const calc = document.getElementById("calculator");

function add(v){
    display.value += v;
}

function clearAll(){
    display.value = "";
}

function del(){
    display.value = display.value.slice(0,-1);
}

function calculate(){
    fetch("/calculate",{
        method:"POST",
        headers:{ "Content-Type":"application/json" },
        body:JSON.stringify({ expr: display.value })
    })
    .then(r=>r.json())
    .then(d=> display.value = d.result);
}

/* ANIMATION FLOW */
setTimeout(()=> mini.classList.add("expand"),2000);
setTimeout(()=>{
    mini.remove();
    calc.classList.remove("hidden");
},2600);
