
import { mount } from '@vue/test-utils';
import Lembretes from '../Lembretes.vue'

describe('Lembretes', () => {
  it('deve renderizar corretamente', async () => {
    const wrapper = mount(Lembretes);

    // Verifica se o componente está sendo renderizado corretamente
    expect(wrapper.exists()).toBe(true);

    // Verifica se os campos de entrada estão sendo exibidos corretamente
    expect(wrapper.find('input[type="text"]').exists()).toBe(true);
    expect(wrapper.find('input[type="date"]').exists()).toBe(true);
  });

  it('deve postar um lembrete quando o formulário é enviado', async () => {
    const wrapper = mount(Lembretes);

    // Simula a entrada de texto nos campos de formulário
    await wrapper.find('input[type="text"]').setValue('Meu lembrete');
    await wrapper.find('input[type="date"]').setValue('2024-04-28');

    // Simula o envio do formulário
    await wrapper.find('form').trigger('submit.prevent');

    // Verifica se o método postLembrete foi chamado corretamente
    expect(wrapper.vm.postLembrete).toHaveBeenCalled();
  });

  it('deve excluir um lembrete quando o botão Excluir é clicado', async () => {
    const wrapper = mount(Lembretes, {
      data() {
        return {
          lembretes: [{ lembrete_id: 1, nome: 'Lembrete de teste', data: '2024-04-28' }]
        };
      }
    });

    // Simula o clique no botão Excluir
    await wrapper.find('button').trigger('click');

    // Verifica se o método excluirLembrete foi chamado corretamente
    expect(wrapper.vm.deleteLembrete).toHaveBeenCalledWith(1);
  });
});

