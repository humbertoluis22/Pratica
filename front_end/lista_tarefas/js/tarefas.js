let inputNovaTarefa = document.querySelector('#inputNovaTarefa');
let btnAddTarefa = document.querySelector('#btnAddtarefa');
let listaTarefa = document.querySelector('#listaTarefas');

let janelaEdicao = document.querySelector('#janelaEdicao')
let janelaEdicaoFundo = document.querySelector('#janelaEdicaoFundo')
let janelaEdicaoBtnFechar = document.querySelector('#janelaEdicaoBtnFechar')
let btnAtualizarTarefa = document.querySelector('#btnAtualizarTarefa')
let idTarefaEdicao = document.querySelector('#idTarefaEdicao')

let inputTarefaNomeEdicao = document.querySelector('#inputTarefaNomeEdicao')


//keycode info o site para ve
inputNovaTarefa.addEventListener('keypress',(e) =>{

    if(e.keycode == 13){
        let tarefa = {
        nome : inputNovaTarefa.value,
        id : gerarId()
        };
        adcionarTarefa(tarefa)
    }
})

btnAddTarefa.addEventListener('click',() =>{

    let tarefa = {
        nome: inputNovaTarefa.value,
        id: gerarId()
    }
    adcionarTarefa(tarefa)

})

function alternarJanelaEdicao(){
    janelaEdicaoFundo.classList.toggle('abrir')
    janelaEdicao.classList.toggle('abrir')
}

janelaEdicaoBtnFechar.addEventListener('click',(e)=>{
    alternarJanelaEdicao()
})


btnAtualizarTarefa.addEventListener('click',(e) =>{
    e.preventDefault()

    let  idTarefa = idTarefaEdicao.innerHTML.replace('#','')

    let tarefa = {
        nome : inputTarefaNomeEdicao.value,
        id : idTarefa
    }

    let tarefaAtual = document.getElementById(''+idTarefa+'')
    if (tarefaAtual){
        let li = criarTagLi(tarefa)
        listaTarefa.replaceChild(li,tarefaAtual)
        alternarJanelaEdicao()
    }else{
        alert('Elemento HTML não encontrado!')
    }

})



function gerarId(){
    return Math.floor(Math.random()*3000);
}

function adcionarTarefa(tarefa){
    let li = criarTagLi(tarefa)
    listaTarefa.appendChild(li)
    inputNovaTarefa.value = '';
    
}

function criarTagLi(tarefa){
    let li = document.createElement('li')
    li.id = tarefa.id

    let span = document.createElement('span')
    span.classList.add('textoTarefa')
    span.innerHTML = tarefa.nome;

    let div = document.createElement('div');

    let btnEditar = document.createElement('button')
    btnEditar.classList.add('btnAcao')
    btnEditar.innerHTML = '<i class="fa fa-pencil"></i>'
    btnEditar.setAttribute('onclick','adicionar('+tarefa.id+')')

    let btnExcluir = document.createElement('button')
    btnExcluir.classList.add('btnAcao')
    btnExcluir.innerHTML = '<i class="fa fa-trash"></i>'
    btnExcluir.setAttribute('onclick','excluir('+tarefa.id+')')

    div.appendChild(btnEditar)
    div.appendChild(btnExcluir)

    li.appendChild(span)
    li.appendChild(div)

    return li

}



function adicionar(idElement){
    let li = document.getElementById(''+idElement+'')
    if(li){
        idTarefaEdicao.innerHTML = '#' + idElement
        inputTarefaNomeEdicao.value = li.innerText 
        alternarJanelaEdicao()

    }else{
        alert('Elemento HTML não encontrado!')
    }
}

function excluir(idElement){
    let confirmacao = window.confirm('Tem Certeza que deseja excluir? ')
    if (confirmacao){
        let li = document.getElementById(''+idElement+'')
        listaTarefa.removeChild(li)
    }else{
        alert('Elemento HTML não encontrado!')
    }
    
}