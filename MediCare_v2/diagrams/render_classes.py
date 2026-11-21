import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
fig,ax=plt.subplots(figsize=(16,11))
fig.patch.set_facecolor('white');ax.set_xlim(0,16);ax.set_ylim(0,12);ax.axis('off')
colors={'entity':('#f1f8fb','#1f526b'),'actor':('#eaf8f3','#147f73'),'service':('#fff7ec','#9d6c32')}
def clazz(x,y,w,h,title,attrs,methods,kind='entity'):
 bg,edge=colors[kind]
 r=FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.015,rounding_size=0.11',edgecolor=edge,facecolor=bg,linewidth=1.4)
 ax.add_patch(r)
 ax.plot([x,x+w],[y+h-.47,y+h-.47],color=edge,lw=1)
 ax.text(x+w/2,y+h-.24,title,fontweight='bold',color=edge,ha='center',va='center',fontsize=11)
 area=[text for text in attrs]
 n=len(area)
 for i,t in enumerate(area):ax.text(x+.15,y+h-.67-i*.26,t,color='#223d4d',fontsize=9.5,va='top')
 div=y+h-.65-len(attrs)*.29-.05
 if methods:
  ax.plot([x,x+w],[div,div],lw=.7,color='#b3cbd5')
  for i,t in enumerate(methods):ax.text(x+.15,div-.19-i*.25,t,fontsize=9.2,color='#223d4d',va='top')
 return (x,y,w,h)
def line(p1,p2,style='solid',txt=None,loc=.55):
 x1,y1=p1;x2,y2=p2
 ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle='-',color='#7995a4',lw=1.45,linestyle=style,connectionstyle='arc3,rad=0'))
 if txt:ax.text(x1+(x2-x1)*loc+.08,y1+(y2-y1)*loc+.12,txt,fontsize=9.2,color='#497084',bbox=dict(fc='white',ec='none',pad=.2))
ax.text(8,11.7,'MediCare  |  Diagrama de classes — v2',ha='center',fontsize=20,fontweight='bold',color='#123a51')
clazz(6.2,9.35,3.6,2.2,'Usuario',['- id: Texto','- nome: Texto','- perfil: PerfilUsuario'],['+ podeExecutar(acao): Booleano'],'actor')
clazz(.55,7.0,4.35,1.75,'Paciente',['- email: Texto'],['+ consultarMinhasConsultas()'],'actor')
clazz(5.95,7.0,4.15,1.75,'Medico',['- especialidade: Texto'],['+ consultarPropriaAgenda()'],'actor')
clazz(11,7.0,4.35,1.75,'Recepcionista',[],['+ agendarPorTelefone()','+ visualizarAgendaGeral()'],'actor')
clazz(.55,3.95,4.65,2.45,'Consulta',['- id: Texto','- dataHora: DataHora','- status: StatusConsulta'],['+ confirmar()','+ cancelar()'])
clazz(6,3.95,4.25,2.45,'Especialidade',['- nome: Texto'],['+ listarMedicos()'])
clazz(11.0,3.95,4.35,2.45,'Atendimento',['- id: Texto','- notaFicticia: Texto'],['+ registrar()'])
clazz(.25,1.0,3.65,1.95,'AgendamentoServico',[],['+ validarDisponibilidade()','+ validar24Horas()','+ confirmar()'],'service')
clazz(4.3,1.0,3.6,1.95,'PainelServico',[],['+ listarPorIdentidade()','+ obterIndicadores()'],'service')
clazz(8.3,1.0,3.6,1.95,'PoliticaAcesso',[],['+ podeConsultar()','+ podeCancelar()','+ podeAtender()'],'service')
clazz(12.3,1.0,3.45,1.95,'ServicoEmailSimulado',[],['+ registrarSolicitacao()'],'service')
line((8,9.35),(2.7,8.75),'dashed','herança')
line((8,9.35),(8,8.75),'dashed','herança')
line((8,9.35),(13.1,8.75),'dashed','herança')
line((2.7,7),(2.7,6.4),txt='1 : 0..* consultas')
line((7.8,7),(4.6,6.4),txt='1 : 0..* consultas',loc=.4)
line((8.6,7),(8.1,6.4),txt='1 especialidade')
line((4.9,4.12),(4.9,3.43))
line((4.9,3.43),(11.1,3.43),txt='1 : 0..1 atendimento',loc=.43)
line((11.1,3.43),(11.1,4.12))
line((2.4,2.95),(2.4,3.95),'dashed')
line((6.1,2.95),(6.1,3.95),'dashed')
line((9.4,2.95),(8,3.95),'dashed')
line((13.8,2.95),(13.8,3.95),'dashed')
ax.text(8,.25,'Associações e cardinalidades modeladas para o protótipo. Herança tracejada; serviços coordenam operações.',ha='center',fontsize=10,color='#587483')
plt.savefig('/mnt/data/MediCare_v2/diagrams/diagrama_classes_v2.png',dpi=145,bbox_inches='tight',pad_inches=.2)
plt.close()
