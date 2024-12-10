// Exemplo de Lista

// ESTRUTURA DE UMA LISTA
List<int> listaDeNumeros = new List<int>();
listaDeNumeros.Add(2);
listaDeNumeros.Add(3);
listaDeNumeros.Add(4);

foreach (int numero in listaDeNumeros)
{
    Console.WriteLine(numero);
};


// ESTRUTURA DE UM DICIONARIO
// Criando um dicionário onde a chave é do tipo string e o valor é do tipo int.

Dictionary<string, int> nomeIdade = new Dictionary<string, int>();
nomeIdade.Add("Humberto", 23);
nomeIdade.Add("Guilherme", 48);

if (nomeIdade.ContainsKey("Maria"))
{
    Console.WriteLine($"a chave maria existe e esta associada a idade de {nomeIdade["Maria"]}");
}
else
{
    Console.WriteLine("A chave maria não existe no dicionario!!");
}

if (nomeIdade.ContainsKey("Humberto"))
{
    Console.WriteLine($"a chave Humberto existe e esta associada a idade de {nomeIdade["Humberto"]} anos");
}
else
{
    Console.WriteLine("A chave Humberto não existe no dicionario!!");
}

// Iterando sobre todos os pares de chave e valor no dicionário.

foreach (KeyValuePair<string, int> pessoa in nomeIdade)
{
    Console.WriteLine($"A pessoa com o nome de {pessoa.Key} tem a idade de {pessoa.Value}");
}

// criando outro para juntar
Dictionary<string, int> nomeIdade2 = new Dictionary<string, int>();
nomeIdade2.Add("Maria", 30);
nomeIdade2.Add("Isabela", 20);
nomeIdade2.Add("Humberto", 20);

Console.WriteLine("*******************************************************************");
foreach (var pessoa2 in nomeIdade2)
{
    if (nomeIdade.ContainsKey(pessoa2.Key))
    {
        Console.WriteLine($"Não foi possivel adicionar a Pessoa {pessoa2.Key} !! ela ja está presente");
    }
    else
    {
        nomeIdade.Add(pessoa2.Key,pessoa2.Value);
    }
}


// adicionando item
nomeIdade.Add("Fulano",0);

//update
nomeIdade["Humberto"] = 24;

// delete
nomeIdade.Remove("Fulano");

foreach(var pessoa in nomeIdade){
    Console.WriteLine(pessoa);
}