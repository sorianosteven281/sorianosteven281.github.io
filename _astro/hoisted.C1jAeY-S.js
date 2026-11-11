import"./hoisted.307Ame_Y.js";document.addEventListener("DOMContentLoaded",()=>{const u=document.getElementById("contact-page-form");if(!u)return;const s=document.getElementById("page-name"),i=document.getElementById("page-company"),l=document.getElementById("page-email"),o=document.getElementById("page-phone"),b=document.getElementById("page-division"),r=document.getElementById("page-message"),f=document.getElementById("page-err-name"),E=document.getElementById("page-err-company"),v=document.getElementById("page-err-email"),y=document.getElementById("page-err-phone"),h=document.getElementById("page-err-msg"),d=document.getElementById("page-modal-success"),I=document.getElementById("page-link-wa"),$=document.getElementById("page-link-mail"),C=document.getElementById("page-btn-close-modal");function t(a,n,e){e?(a.classList.add("border-red-500","bg-red-950/20"),a.classList.remove("border-white/[0.1]"),n?.classList.remove("hidden")):(a.classList.remove("border-red-500","bg-red-950/20"),a.classList.add("border-white/[0.1]"),n?.classList.add("hidden"))}s?.addEventListener("input",()=>t(s,f,!1)),i?.addEventListener("input",()=>t(i,E,!1)),l?.addEventListener("input",()=>t(l,v,!1)),o?.addEventListener("input",()=>t(o,y,!1)),r?.addEventListener("input",()=>t(r,h,!1)),u.addEventListener("submit",a=>{a.preventDefault();let n=!1,e=null;const m=s?.value.trim()||"";m.length<3&&(t(s,f,!0),n=!0,e||(e=s));const c=i?.value.trim()||"";c.length<2&&(t(i,E,!0),n=!0,e||(e=i));const g=l?.value.trim()||"";/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(g)||(t(l,v,!0),n=!0,e||(e=l)),(o?.value.replace(/\D/g,"")||"").length<7&&(t(o,y,!0),n=!0,e||(e=o));const p=r?.value.trim()||"";if(p.length<8&&(t(r,h,!0),n=!0,e||(e=r)),n){e?.focus();return}const B=b?.value||"General",D=`*Requerimiento Técnico - CB Soluciones*

*Contacto:* ${m}
*Empresa:* ${c}
*Correo:* ${g}
*Teléfono:* ${o.value.trim()}
*Especialidad:* ${B}

*Detalle:* ${p}`,L=`https://wa.me/51982721661?text=${encodeURIComponent(D)}`,w=`mailto:servicios@perucb.com?subject=${encodeURIComponent(`Cotización: ${c} - ${m}`)}&body=${encodeURIComponent(`Nombre: ${m}
Empresa: ${c}
Email: ${g}
Teléfono: ${o.value.trim()}
Servicio: ${B}

Detalle:
${p}`)}`;I&&(I.href=L),$&&($.href=w),d&&d.classList.remove("hidden"),window.open(L,"_blank")}),C?.addEventListener("click",()=>{d&&d.classList.add("hidden"),u.reset()})});
