document.addEventListener("DOMContentLoaded", () => {
  const items = document.querySelectorAll('.sidebar ul li[data-view]');
  const container = document.getElementById('view-container');

  // Função para carregar o conteúdo do arquivo HTML da view
  async function loadView(view) {
    try {
      const response = await fetch(`views/${view}.html`);
      if (!response.ok) {
        container.innerHTML = `<p>Erro ao carregar a view "${view}".</p>`;
        return;
      }
      const html = await response.text();
      container.innerHTML = html;
    } catch (error) {
      container.innerHTML = `<p>Erro ao carregar a view "${view}": ${error.message}</p>`;
    }
  }

  items.forEach(item => {
    item.addEventListener('click', () => {
      document.querySelectorAll('.sidebar ul li').forEach(i => i.classList.remove('active'));
      item.classList.add('active');

      const view = item.getAttribute('data-view');
      loadView(view);
    });
  });

  // Carrega a view padrão
  loadView('dashboard');
});
