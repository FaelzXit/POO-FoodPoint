function atualizarContadoresSeparacao() {
    const agora = Math.floor(Date.now() / 1000);

    document.querySelectorAll(".contador-separacao").forEach((contador) => {
        const inicio = Number(contador.dataset.inicio);
        if (!Number.isFinite(inicio)) {
            contador.textContent = "00:00";
            return;
        }

        const totalSegundos = Math.max(0, agora - inicio);
        const horas = Math.floor(totalSegundos / 3600);
        const minutos = Math.floor((totalSegundos % 3600) / 60);
        const segundos = totalSegundos % 60;
        const doisDigitos = (valor) => String(valor).padStart(2, "0");

        contador.textContent = horas > 0
            ? `${doisDigitos(horas)}:${doisDigitos(minutos)}:${doisDigitos(segundos)}`
            : `${doisDigitos(minutos)}:${doisDigitos(segundos)}`;
    });
}

atualizarContadoresSeparacao();
window.setInterval(atualizarContadoresSeparacao, 1000);
