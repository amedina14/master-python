'use strict'

const nome = "Adrian Medina";
const altezza = 190;

/*
if (altezza > 180){
    document.write();
} else{
    document.write();
}
*/

function template(nome,altezza){
    let dato = `
    <p>Nome: ${nome}</p>
    <p>Altezza: ${altezza}</p>
    `;
    return dato;
}



function stampa(){
    let dato = document.getElementById("dato");
    dato.innerHTML = template(nome,altezza);
}

stampa();


/*
const luogo_articolo = document.querySelector(".articoli");
luogo_articolo.innerHTML = articolo;

let dato = document.getElementById("articoli");
dato.innerHTML = lista[i];

*/

function temp_articolo(){
    let articolo = `
    <article>
    <h2>Titolo articolo</h2>
    <p>Testo del parragrago</p>
    </article>
    `;
    return articolo;
}

function stampa_cose(i){
    return document.write(cose[i]+"<br/>");
}

function ciclo(){
    let result="";
    for(let i = 0; i <= 3; i++){
        result += temp_articolo();
    }
    return result;
}

//div_cose.innerHTML = temp_articolo();
const div_cose = document.querySelector("#cose");
div_cose.innerHTML = ciclo();

const cose = ['casa','macchina','cibo'];
for(let i = 0; i < cose.length; i++){
    document.write(cose[i]+" ");
}



