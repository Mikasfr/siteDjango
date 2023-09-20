  // Referenciar os elementos do formulário e o botão
  const formulario = document.querySelector('.form');
  const quantidadeInput = formulario.querySelector('input[name="quantidade"]');
  const codigoInput = formulario.querySelector('input[name="codigo"]');
  const descricaoInput = formulario.querySelector('input[name="descricao"]');
  const aplicacaoInput = formulario.querySelector('input[name="aplicacao"]');
  const valorInput = formulario.querySelector('input[name="valor"]');
  const botaoEnviar = formulario.querySelector('.submit button');

  // Função para mostrar um alerta de sucesso
  function mostrarAlertaDeSucesso() {
    alert('Dados enviados com sucesso!');
  }

  // Função para verificar se todos os campos estão preenchidos
  function verificarCamposPreenchidos() {
    if (
      quantidadeInput.value.trim() !== '' &&
      codigoInput.value.trim() !== '' &&
      descricaoInput.value.trim() !== '' &&
      aplicacaoInput.value.trim() !== '' &&
      valorInput.value.trim() !== ''
    ) {
      botaoEnviar.removeAttribute('disabled');
    } else {
      botaoEnviar.setAttribute('disabled', 'true');
    }
  }

  // Adicionar um ouvinte de eventos para o envio do formulário
  formulario.addEventListener('submit', function (event) {
    event.preventDefault(); // Impede o envio padrão do formulário
    // Aqui você pode adicionar a lógica de envio do formulário para o servidor, se necessário

    // Mostrar o alerta de sucesso
    mostrarAlertaDeSucesso();

    // Limpar os campos ou fazer outras ações necessárias após o envio
    quantidadeInput.value = '';
    codigoInput.value = '';
    descricaoInput.value = '';
    aplicacaoInput.value = '';
    valorInput.value = '';
    
    // Verificar novamente os campos preenchidos
    verificarCamposPreenchidos();
  });

  // Verifique o estado inicial dos campos
  verificarCamposPreenchidos();