import"./hoisted.DiVcdJv8.js";document.addEventListener("DOMContentLoaded",()=>{const c=document.getElementById("corp-form");if(!c)return;const v=document.getElementById("c-name"),y=document.getElementById("c-company"),I=document.getElementById("c-email"),B=document.getElementById("c-phone"),L=document.getElementById("c-service"),$=document.getElementById("c-msg"),l=document.getElementById("c-err-name"),a=document.getElementById("c-err-company"),r=document.getElementById("c-err-email"),u=document.getElementById("c-err-phone"),p=document.getElementById("c-err-service"),g=document.getElementById("c-err-msg"),t=document.getElementById("corp-modal"),h=document.getElementById("corp-wa"),E=document.getElementById("corp-mail"),C=document.getElementById("corp-close");c.addEventListener("submit",b=>{b.preventDefault();let e=!0;const n=(v?.value||"").trim(),s=(y?.value||"").trim(),o=(I?.value||"").trim(),d=(B?.value||"").trim(),i=L?.value||"",m=($?.value||"").trim();if(n.length<3?(l?.classList.remove("hidden"),e=!1):l?.classList.add("hidden"),s.length<2?(a?.classList.remove("hidden"),e=!1):a?.classList.add("hidden"),/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(o)?r?.classList.add("hidden"):(r?.classList.remove("hidden"),e=!1),d.replace(/\D/g,"").length<7?(u?.classList.remove("hidden"),e=!1):u?.classList.add("hidden"),i?p?.classList.add("hidden"):(p?.classList.remove("hidden"),e=!1),m.length<8?(g?.classList.remove("hidden"),e=!1):g?.classList.add("hidden"),!e)return;const w=`*Requerimiento Técnico - CB Soluciones*

*Contacto:* ${n}
*Empresa / Mina:* ${s}
*Correo:* ${o}
*Teléfono:* ${d}
*Especialidad:* ${i}

*Alcance:* ${m}`,f=`https://wa.me/51982721661?text=${encodeURIComponent(w)}`,M=`mailto:servicios@perucb.com?subject=${encodeURIComponent(`Requerimiento: ${s} - ${n}`)}&body=${encodeURIComponent(`Nombre: ${n}
Empresa: ${s}
Email: ${o}
Teléfono: ${d}
Servicio: ${i}

Alcance:
${m}`)}`;h&&(h.href=f),E&&(E.href=M),t&&t.classList.remove("hidden"),window.open(f,"_blank")}),C?.addEventListener("click",()=>{t&&t.classList.add("hidden"),c.reset()})});
