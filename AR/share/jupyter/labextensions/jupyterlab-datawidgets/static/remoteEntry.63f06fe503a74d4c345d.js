var _JUPYTERLAB;(()=>{"use strict";var e,r,t,a,n,o,i,u,l,s,d,f,p,c,h,v,b,g,m={614:(e,r,t)=>{var a={"./index":()=>Promise.all([t.e(170),t.e(880)]).then((()=>()=>t(880))),"./extension":()=>Promise.all([t.e(170),t.e(880)]).then((()=>()=>t(880)))},n=(e,r)=>(t.R=r,r=t.o(a,e)?a[e]():Promise.resolve().then((()=>{throw new Error('Module "'+e+'" does not exist in container.')})),t.R=void 0,r),o=(e,r)=>{if(t.S){var a="default",n=t.S[a];if(n&&n!==e)throw new Error("Container initialization failed as it has already been initialized with a different share scope");return t.S[a]=e,t.I(a,r)}};t.d(r,{get:()=>n,init:()=>o})}},y={};function w(e){var r=y[e];if(void 0!==r)return r.exports;var t=y[e]={exports:{}};return m[e].call(t.exports,t,t.exports,w),t.exports}w.m=m,w.c=y,w.d=(e,r)=>{for(var t in r)w.o(r,t)&&!w.o(e,t)&&Object.defineProperty(e,t,{enumerable:!0,get:r[t]})},w.f={},w.e=e=>Promise.all(Object.keys(w.f).reduce(((r,t)=>(w.f[t](e,r),r)),[])),w.u=e=>e+"."+{170:"37e48feceae1c16a28e2",511:"22f7942246884696c751",824:"9dfde28e806c4451c997",880:"b9ae0dbdfd88fcbf13dc"}[e]+".js?v="+{170:"37e48feceae1c16a28e2",511:"22f7942246884696c751",824:"9dfde28e806c4451c997",880:"b9ae0dbdfd88fcbf13dc"}[e],w.g=function(){if("object"==typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(e){if("object"==typeof window)return window}}(),w.o=(e,r)=>Object.prototype.hasOwnProperty.call(e,r),e={},r="jupyterlab-datawidgets:",w.l=(t,a,n,o)=>{if(e[t])e[t].push(a);else{var i,u;if(void 0!==n)for(var l=document.getElementsByTagName("script"),s=0;s<l.length;s++){var d=l[s];if(d.getAttribute("src")==t||d.getAttribute("data-webpack")==r+n){i=d;break}}i||(u=!0,(i=document.createElement("script")).charset="utf-8",i.timeout=120,w.nc&&i.setAttribute("nonce",w.nc),i.setAttribute("data-webpack",r+n),i.src=t),e[t]=[a];var f=(r,a)=>{i.onerror=i.onload=null,clearTimeout(p);var n=e[t];if(delete e[t],i.parentNode&&i.parentNode.removeChild(i),n&&n.forEach((e=>e(a))),r)return r(a)},p=setTimeout(f.bind(null,void 0,{type:"timeout",target:i}),12e4);i.onerror=f.bind(null,i.onerror),i.onload=f.bind(null,i.onload),u&&document.head.appendChild(i)}},(()=>{w.S={};var e={},r={};w.I=(t,a)=>{a||(a=[]);var n=r[t];if(n||(n=r[t]={}),!(a.indexOf(n)>=0)){if(a.push(n),e[t])return e[t];w.o(w.S,t)||(w.S[t]={});var o=w.S[t],i="jupyterlab-datawidgets",u=(e,r,t,a)=>{var n=o[e]=o[e]||{},u=n[r];(!u||!u.loaded&&(!a!=!u.eager?a:i>u.from))&&(n[r]={get:t,from:i,eager:!!a})},l=[];return"default"===t&&(u("jupyter-datawidgets","5.5.2",(()=>Promise.all([w.e(511),w.e(824),w.e(170)]).then((()=>()=>w(824))))),u("jupyterlab-datawidgets","7.1.2",(()=>Promise.all([w.e(170),w.e(880)]).then((()=>()=>w(880)))))),e[t]=l.length?Promise.all(l).then((()=>e[t]=1)):1}}})(),(()=>{var e;w.g.importScripts&&(e=w.g.location+"");var r=w.g.document;if(!e&&r&&(r.currentScript&&(e=r.currentScript.src),!e)){var t=r.getElementsByTagName("script");t.length&&(e=t[t.length-1].src)}if(!e)throw new Error("Automatic publicPath is not supported in this browser");e=e.replace(/#.*$/,"").replace(/\?.*$/,"").replace(/\/[^\/]+$/,"/"),w.p=e})(),t=e=>{var r=e=>e.split(".").map((e=>+e==e?+e:e)),t=/^([^-+]+)?(?:-([^+]+))?(?:\+(.+))?$/.exec(e),a=t[1]?r(t[1]):[];return t[2]&&(a.length++,a.push.apply(a,r(t[2]))),t[3]&&(a.push([]),a.push.apply(a,r(t[3]))),a},a=(e,r)=>{e=t(e),r=t(r);for(var a=0;;){if(a>=e.length)return a<r.length&&"u"!=(typeof r[a])[0];var n=e[a],o=(typeof n)[0];if(a>=r.length)return"u"==o;var i=r[a],u=(typeof i)[0];if(o!=u)return"o"==o&&"n"==u||"s"==u||"u"==o;if("o"!=o&&"u"!=o&&n!=i)return n<i;a++}},n=e=>{var r=e[0],t="";if(1===e.length)return"*";if(r+.5){t+=0==r?">=":-1==r?"<":1==r?"^":2==r?"~":r>0?"=":"!=";for(var a=1,o=1;o<e.length;o++)a--,t+="u"==(typeof(u=e[o]))[0]?"-":(a>0?".":"")+(a=2,u);return t}var i=[];for(o=1;o<e.length;o++){var u=e[o];i.push(0===u?"not("+l()+")":1===u?"("+l()+" || "+l()+")":2===u?i.pop()+" "+i.pop():n(u))}return l();function l(){return i.pop().replace(/^\((.+)\)$/,"$1")}},o=(e,r)=>{if(0 in e){r=t(r);var a=e[0],n=a<0;n&&(a=-a-1);for(var i=0,u=1,l=!0;;u++,i++){var s,d,f=u<e.length?(typeof e[u])[0]:"";if(i>=r.length||"o"==(d=(typeof(s=r[i]))[0]))return!l||("u"==f?u>a&&!n:""==f!=n);if("u"==d){if(!l||"u"!=f)return!1}else if(l)if(f==d)if(u<=a){if(s!=e[u])return!1}else{if(n?s>e[u]:s<e[u])return!1;s!=e[u]&&(l=!1)}else if("s"!=f&&"n"!=f){if(n||u<=a)return!1;l=!1,u--}else{if(u<=a||d<f!=n)return!1;l=!1}else"s"!=f&&"n"!=f&&(l=!1,u--)}}var p=[],c=p.pop.bind(p);for(i=1;i<e.length;i++){var h=e[i];p.push(1==h?c()|c():2==h?c()&c():h?o(h,r):!c())}return!!c()},i=(e,r)=>{var t=w.S[e];if(!t||!w.o(t,r))throw new Error("Shared module "+r+" doesn't exist in shared scope "+e);return t},u=(e,r)=>{var t=e[r];return Object.keys(t).reduce(((e,r)=>!e||!t[e].loaded&&a(e,r)?r:e),0)},l=(e,r,t,a)=>"Unsatisfied version "+t+" from "+(t&&e[r][t].from)+" of shared singleton module "+r+" (required "+n(a)+")",s=(e,r,t,a)=>{var n=u(e,t);return o(a,n)||"undefined"!=typeof console&&console.warn&&console.warn(l(e,t,n,a)),f(e[t][n])},d=(e,r,t)=>{var n=e[r];return(r=Object.keys(n).reduce(((e,r)=>!o(t,r)||e&&!a(e,r)?e:r),0))&&n[r]},f=e=>(e.loaded=1,e.get()),c=(p=e=>function(r,t,a,n){var o=w.I(r);return o&&o.then?o.then(e.bind(e,r,w.S[r],t,a,n)):e(r,w.S[r],t,a,n)})(((e,r,t,a)=>(i(e,t),s(r,0,t,a)))),h=p(((e,r,t,a,n)=>{var o=r&&w.o(r,t)&&d(r,t,a);return o?f(o):n()})),v={},b={170:()=>c("default","@jupyter-widgets/base",[,[1,6,0,0],[1,5],[1,4],[1,3],[1,2],[1,1],1,1,1,1,1]),526:()=>c("default","@lumino/coreutils",[1,1,11,0]),741:()=>h("default","jupyter-datawidgets",[1,5,5,2],(()=>Promise.all([w.e(511),w.e(824)]).then((()=>()=>w(824)))))},g={170:[170],880:[526,741]},w.f.consumes=(e,r)=>{w.o(g,e)&&g[e].forEach((e=>{if(w.o(v,e))return r.push(v[e]);var t=r=>{v[e]=0,w.m[e]=t=>{delete w.c[e],t.exports=r()}},a=r=>{delete v[e],w.m[e]=t=>{throw delete w.c[e],r}};try{var n=b[e]();n.then?r.push(v[e]=n.then(t).catch(a)):t(n)}catch(e){a(e)}}))},(()=>{var e={575:0};w.f.j=(r,t)=>{var a=w.o(e,r)?e[r]:void 0;if(0!==a)if(a)t.push(a[2]);else if(170!=r){var n=new Promise(((t,n)=>a=e[r]=[t,n]));t.push(a[2]=n);var o=w.p+w.u(r),i=new Error;w.l(o,(t=>{if(w.o(e,r)&&(0!==(a=e[r])&&(e[r]=void 0),a)){var n=t&&("load"===t.type?"missing":t.type),o=t&&t.target&&t.target.src;i.message="Loading chunk "+r+" failed.\n("+n+": "+o+")",i.name="ChunkLoadError",i.type=n,i.request=o,a[1](i)}}),"chunk-"+r,r)}else e[r]=0};var r=(r,t)=>{var a,n,[o,i,u]=t,l=0;if(o.some((r=>0!==e[r]))){for(a in i)w.o(i,a)&&(w.m[a]=i[a]);u&&u(w)}for(r&&r(t);l<o.length;l++)n=o[l],w.o(e,n)&&e[n]&&e[n][0](),e[n]=0},t=self.webpackChunkjupyterlab_datawidgets=self.webpackChunkjupyterlab_datawidgets||[];t.forEach(r.bind(null,0)),t.push=r.bind(null,t.push.bind(t))})();var j=w(614);(_JUPYTERLAB=void 0===_JUPYTERLAB?{}:_JUPYTERLAB)["jupyterlab-datawidgets"]=j})();