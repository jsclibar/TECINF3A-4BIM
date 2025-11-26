// Esta função será chamada quando o usuário clicar no botão "Calcular"
function calcularIdade() {

    // Pegamos o valor digitado no campo "nome"
    const nome = document.getElementById("nome").value;

    // Pegamos a data escolhida no campo "dataNascimento"
    const data = document.getElementById("dataNascimento").value;

    // Verifica se o usuário deixou algum campo vazio
    if (!nome || !data) {
        document.getElementById("resultado").innerText =
            "Por favor, preencha o nome e a data de nascimento.";
        return; // Interrompe a função se os dados estiverem incompletos
    }

    // Converte a data de nascimento (texto) para um objeto Date do JavaScript
    const dataNasc = new Date(data);

    // Pega a data atual do sistema (hoje)
    const hoje = new Date();

    // Calcula a idade inicial apenas pela diferença dos anos
    let idade = hoje.getFullYear() - dataNasc.getFullYear();

    // Calcula a diferença de meses entre hoje e a data de nascimento
    const diferencaMes = hoje.getMonth() - dataNasc.getMonth();

    /* 
       Agora vamos ajustar a idade se a pessoa ainda NÃO fez aniversário este ano.
       Isso ocorre quando:
       - O mês atual é menor que o mês de nascimento
       OU
       - O mês é igual, mas o dia atual é menor que o dia de nascimento
    */
    if (diferencaMes < 0 || 
        (diferencaMes === 0 && hoje.getDate() < dataNasc.getDate())) {
        idade--;  // Ainda não fez aniversário → diminui 1 ano
    }

    // Exibe a mensagem final no parágrafo com id="resultado"
    document.getElementById("resultado").innerText =
        `${nome}, você tem ${idade} anos.`;
}