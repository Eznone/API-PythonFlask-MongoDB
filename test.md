Test para GET:
  * So rodar com nada no json do REQBIN


Test para POST:
  * Insere o seguinte no json do REQBIN
  * {
      "titulo": "ENG4431",
      "descricao": "Testing knowledge on creating an API",
      "status": "nao",
      "data-entrega": "9/18/23"
    }
  * Ele vai dar devolta todos os dados incluindo um novo sendo o _id que precisa para fazer o DELETE dessa tarefa

Test para PUT:
  * Esse proximo vai ter que ser com um dado eu ja tinha colocado no meu mongoDB porque o anterior que acabou de ser inserido a gente nao vai saber o ID se a gente nao for entrar na minha conta do banco de dados
  * Insere o seguinte no json do REQBIN
  * {
      "_id": "6502698747517b9b84759e0a",
      "titulo": "ENG4431",
      "descricao": "work",
      "status": "nao",
      "data-entrega": "9/18/23"
    }
  * E sim o site vai devolver os dados do novo atualizacao incluindo o id


Test para DELETE:
  * Insere o seguinte no URL do REQBIN
  * https://atividade-05-api-de-tarefas-enzomediano.eng4431-20232.repl.co/tarefas/<id que pegou do POST>
  * Ele so vai retornar um mensagem falando que o documento foi deletado