from database import registrar_tempo_etapa, listar_historico_etapas

registrar_tempo_etapa(7, "Finalização", 5)

historico = listar_historico_etapas()
print(historico)