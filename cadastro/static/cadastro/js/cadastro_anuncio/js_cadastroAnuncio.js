preco_field = document.getElementById('id_preco');
var val_atual = '';
var added_dot = false;

function dot_to_right(string) {
    if (added_dot) {
        if (string.includes('.')) {
            /* comprimento é maior que 3 pois ja foi add ponto */
            splited_string = string.split('.');
            let parte_centavo = splited_string[1];
            let parte_real = splited_string[0] + parte_centavo.charAt(0);

            parte_centavo = parte_centavo.slice(1, parte_centavo.length);

            console.log('COM PONTO      real => ' + String(parte_real) + '       | centavo => ' + String(parte_centavo));
            let string_with_right_dot = String(parte_real) + '.' + String(parte_centavo);
            string = string_with_right_dot;
        } else {
            added_dot = false;
        }
    } else {
        added_dot = true;
        let parte_real = string.slice(0, string.length);
        let parte_centavo = string.slice(string.length - 1, string.length);
        console.log('SEM PONTO      real => ' + String(parte_real) + '       | centavo => ' + String(parte_centavo));
        string = String(parte_real) + '.' + String(parte_centavo);
    }
    return string
}

/* preco_field.oninput = () => {
    var value = preco_field.value;
    var len_value = value.length;
    if (len_value > 2) {
        preco_field.value = dot_to_right(preco_field.value);
    }
} */

expositor = document.getElementById('expositor-meu');

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
    })
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
add_(1);
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