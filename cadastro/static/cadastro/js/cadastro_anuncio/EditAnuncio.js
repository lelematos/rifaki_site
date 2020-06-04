var img_input_1 = document.getElementById('id_imagem1');
var img_input_2 = document.getElementById('id_imagem2');
var img_input_3 = document.getElementById('id_imagem3');
var img_input_4 = document.getElementById('id_imagem4');
var img_input_5 = document.getElementById('id_imagem5');
var list_img_inputs = [img_input_1, img_input_2, img_input_3, img_input_4, img_input_5];

var list_outputs = document.getElementsByClassName('output_image');

function limpa_img_input(index) {
    list_img_inputs[index].value = '';
    list_outputs[index].src = '';
}

function preview_imagem(event, index) {
    var reader = new FileReader();
    reader.onload = function () {
        var output = document.getElementsByClassName('output_image');
        var output_index = output[index];
        output_index.src = reader.result;
    }
    reader.readAsDataURL(event.target.files[0]);
}

function addEventImgInputs(index) {
    list_img_inputs[index].addEventListener('change', () => {
        preview_imagem(event, index);
    });
}

addEventImgInputs(0);
addEventImgInputs(1);
addEventImgInputs(2);
addEventImgInputs(3);
addEventImgInputs(4);


/* secao form */


const floatField1 = document.getElementById('id_titulo_anuncio');
const floatField2 = document.getElementById('id_ano_fabricacao');
const floatField3 = document.getElementById('id_descricao_breve');
const floatField4 = document.getElementById('id_descricao_completa');
const floatField5 = document.getElementById('id_preco');
var list_fields = [floatField1, floatField2, floatField3, floatField4, floatField5];

const floatContainer = document.getElementsByClassName('float-container');

/* preview functions */
const labels_substituicao = document.getElementsByClassName('substituir');

// estilizando o seletor de cor 
var seletor = document.getElementById('id_text_color');
seletor.classList.add('uk-select');

function alteraCorDoTexto(label, cor) {
    let string_cor = 'color: ' + String(cor) + ';';
    label.setAttribute('style', string_cor);
}

// altera cor do text de acordo com a selecao
seletor.addEventListener('change', () => {
    console.log('mudei')
    // cor do titulo:
    alteraCorDoTexto(labels_substituicao[0], seletor.value);
    // cor da descricao breve:
    alteraCorDoTexto(labels_substituicao[1], seletor.value);
});


/* ---------------- */

floatField2.setAttribute("placeholder", 'Ex.: 1998');
floatField2.setAttribute("type", '');

floatField5.setAttribute("placeholder", 'Ex.: 20.00 (Use ponto e não vírgula!)');
floatField5.setAttribute("type", '');


/* functions */
function add_(i) {
    floatContainer[i].classList.add('active');
}

function remove_(i) {
    floatContainer[i].classList.remove('active');
}

function atualizaLabel(primary_label, substitution_label) {
    substitution_label.innerHTML = ''
    substitution_label.appendChild(document.createTextNode(primary_label.value)) /* será passado um v_algumaCoisa (primary_label) */
}
/* --------- */


/* atribuições iniciais */
add_(0);
add_(1);
add_(3);
add_(2);
atualizaLabel(list_fields[0], labels_substituicao[0]);
atualizaLabel(list_fields[2], labels_substituicao[1]);
atualizaLabel(list_fields[3], labels_substituicao[2]);
// cor do titulo:
alteraCorDoTexto(labels_substituicao[0], seletor.value);
// cor da descricao breve:
alteraCorDoTexto(labels_substituicao[1], seletor.value);
/* -------------------- */


/* EVENT LISTENERS */
list_fields[0].addEventListener('focus', () => {
    add_(0);
});

list_fields[0].addEventListener('blur', () => {
    atualizaLabel(list_fields[0], labels_substituicao[0]);
    if (list_fields[0].value === '') {
        remove_(0)
    }

});

list_fields[2].addEventListener('focus', () => {
    add_(2);
});

list_fields[2].addEventListener('blur', () => {
    atualizaLabel(list_fields[2], labels_substituicao[1]);
    if (list_fields[2].value === '') {
        remove_(2)
    }
});
list_fields[3].addEventListener('focus', () => {
    add_(3);
});

list_fields[3].addEventListener('blur', () => {
    atualizaLabel(list_fields[3], labels_substituicao[2]);
    if (list_fields[3].value === '') {
        remove_(3)
    }
});