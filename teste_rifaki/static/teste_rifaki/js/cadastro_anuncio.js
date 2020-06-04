var btn_submit = document.querySelector(".submit-anuncio");
var input_desc_breve = document.querySelector(".form-cadastro-anuncio input[name=desc-breve-anuncio]");
var input_desc_completa = document.querySelector(".form-cadastro-anuncio input[name=desc-completa-anuncio]");
var input_titulo = document.querySelector(".form-cadastro-anuncio input[name=titulo-anuncio]");
var input_img = document.querySelector(".form-cadastro-anuncio input[name=imagens-anuncio]")

var list_inputs_meu = [input_titulo, input_desc_breve, input_desc_completa]; /* terá um sequencia de infos */

/* var anuncio1 = { 
    titulo: "",
    descricao_breve: "", 
    descricao_completa: "", 
    imagens: [],
} */

function le_titulo(list_inputs){
    return list_inputs[0].value;
}

function le_desc_breve(list_inputs){
    return list_inputs[1].value;
}

function le_descricao_completa(list_inputs){
    return list_inputs[2].value;
}

function atualiza_inputs(list_inputs){
    var anuncio = {
/*      titulo: "",
        descricao_breve: "", 
        descricao_completa: "", 
        imagens: [],                */
    } 
    anuncio.titulo = le_titulo(list_inputs);
    anuncio.descricao_breve = le_desc_breve(list_inputs);
    anuncio.descricao_completa = le_descricao_completa(list_inputs);
    console.log(anuncio);
    return anuncio
}

btn_submit.onclick = function(){
    atualiza_inputs(list_inputs_meu);
}

