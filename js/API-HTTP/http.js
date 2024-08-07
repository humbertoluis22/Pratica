// if(self.fetch){
//     console.log('Tem suporte')
//     fetch('https://jsonplaceholder.typicode.com/todos/1')
//     .then(response => response.json())
//     .then(json => console.log(json))
    
// }else{
//     console.log('Não tem suporte')
// }


if (self.fetch){
    console.log('Tem suporte');
    (async() =>{
        // let json = await obterPost(1)

        // let json = await incluirPost({
        //     userId : 1,
        //     title: 'Meu post',
        //     body: 'Meu conteudo exemplo'
        // });

        // let json = await atualizarPost({
        //     userId : 1,
        //     title: 'Meu post',
        //     body: 'Meu conteudo exemplo'
        // },1);

        let json  = await deletarPost(1)
        console.log(json)
    })()
    // console.log(obterPost(1))
}else{
     console.log('Não tem suporte')
    }


async function obterJsonResposta(resposta){
    if (!resposta.ok){
        throw new Error(
            `${resposta.status} - ${resposta.statusText}`
        );
    }
    let json = await resposta.json();
    return json;
}


async function obterPost(id){
    let resposta = await fetch('https://jsonplaceholder.typicode.com/posts/'+id)
    return obterJsonResposta(resposta)
}


async function incluirPost(data){
    const resposta = 
    await fetch('https://jsonplaceholder.typicode.com/posts/',{
        method:'POST',
        body : JSON.stringify(data),
        headers : {
            'Content-type':'application/json;charset=UTF-8'
        }

    });
    return obterJsonResposta(resposta)
}

async function atualizarPost(data,id){
    const resposta = 
    await fetch('https://jsonplaceholder.typicode.com/posts/' + id,{
        method:'PUT',
        body : JSON.stringify(data),
        headers : {
            'Content-type':'application/json;charset=UTF-8'
        }

    });
    return obterJsonResposta(resposta)
}

async function deletarPost(id){
    let resposta = 
    await fetch('https://jsonplaceholder.typicode.com/posts/' + id,{
        method : 'DELETE',
        headers:{
            'Content-type':'application/json;charset-UTF-8'
        }
    })
    return obterJsonResposta(resposta)
}