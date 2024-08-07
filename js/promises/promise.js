// executa codigo assincrono async
// tres status
// pendente
// resolvido
// rejeitado 
// lembrando que é uma promessa, ou seja pode nao ter uma resposta 

//         *** codigo para exemplo *** 
// let p1 = new Promise((resolve,reject) => {
//     setTimeout(()=>{
//         resolve('Promise deu certo')
//     },4000);
// }).then(resp => console.log(resp))

// console.log('Primeira exibição');

let numero= 10

function encontra_numero(numero,maxNumero){
    return new Promise((resolve,reject) => {
        console.log('Max numero é '+ maxNumero)
        for(let i = 0 ; i < maxNumero;i++){
            if(i == numero){
                resolve(numero)
            }
        }
        reject(numero)
    })
}

const encontraNumero1 = 
encontra_numero(numero,Math.ceil(Math.random() * 20 ))

// codigo de exemplo 
// encontraNumero1.then((resp)=>{
//     console.log('Numero resolvido : ' + resp)
// }).catch((err) => {
//     console.log('Não resolvido : '+ err)
// })

const encontraNumero2 = 
encontra_numero(numero,Math.ceil(Math.random() * 50 ))

// precisa localizar todas as promisses
Promise.all([
    encontraNumero1,
    encontraNumero2
]).then((rep) =>{
    console.log('OK,encontrou todas as promisses',rep)
}).catch((err) => {
    console.log('Falhou : ',err)
})

// para que só uma promisses seja encontrada
// utilizamos o any no lucar do all