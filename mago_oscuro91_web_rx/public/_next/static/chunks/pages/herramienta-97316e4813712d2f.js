(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[152],{1558:function(e,t,a){(window.__NEXT_P=window.__NEXT_P||[]).push(["/herramienta",function(){return a(8786)}])},1342:function(e,t,a){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),function(e,t){for(var a in t)Object.defineProperty(e,a,{enumerable:!0,get:t[a]})}(t,{noSSR:function(){return noSSR},default:function(){return dynamic}});let r=a(8754),n=(a(7294),r._(a(4304)));function convertModule(e){return{default:(null==e?void 0:e.default)||e}}function noSSR(e,t){return delete t.webpack,delete t.modules,e(t)}function dynamic(e,t){let a=n.default,r={loading:e=>{let{error:t,isLoading:a,pastDelay:r}=e;return null}};e instanceof Promise?r.loader=()=>e:"function"==typeof e?r.loader=e:"object"==typeof e&&(r={...r,...e}),r={...r,...t};let i=r.loader;return(r.loadableGenerated&&(r={...r,...r.loadableGenerated},delete r.loadableGenerated),"boolean"!=typeof r.ssr||r.ssr)?a({...r,loader:()=>null!=i?i().then(convertModule):Promise.resolve(convertModule(()=>null))}):(delete r.webpack,delete r.modules,noSSR(a,r))}("function"==typeof t.default||"object"==typeof t.default&&null!==t.default)&&void 0===t.default.__esModule&&(Object.defineProperty(t.default,"__esModule",{value:!0}),Object.assign(t.default,t),e.exports=t.default)},43:function(e,t,a){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),Object.defineProperty(t,"LoadableContext",{enumerable:!0,get:function(){return i}});let r=a(8754),n=r._(a(7294)),i=n.default.createContext(null)},4304:function(e,t,a){"use strict";/**
@copyright (c) 2017-present James Kyle <me@thejameskyle.com>
 MIT License
 Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:
 The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.
 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE
*/Object.defineProperty(t,"__esModule",{value:!0}),Object.defineProperty(t,"default",{enumerable:!0,get:function(){return c}});let r=a(8754),n=r._(a(7294)),i=a(43);function resolve(e){return e&&e.default?e.default:e}let o=[],s=[],l=!1;function load(e){let t=e(),a={loading:!0,loaded:null,error:null};return a.promise=t.then(e=>(a.loading=!1,a.loaded=e,e)).catch(e=>{throw a.loading=!1,a.error=e,e}),a}function createLoadableComponent(e,t){let a=Object.assign({loader:null,loading:null,delay:200,timeout:null,webpack:null,modules:null},t),r=null;function init(){if(!r){let t=new LoadableSubscription(e,a);r={getCurrentValue:t.getCurrentValue.bind(t),subscribe:t.subscribe.bind(t),retry:t.retry.bind(t),promise:t.promise.bind(t)}}return r.promise()}if(!l){let e=a.webpack?a.webpack():a.modules;e&&s.push(t=>{for(let a of e)if(t.includes(a))return init()})}function useLoadableModule(){init();let e=n.default.useContext(i.LoadableContext);e&&Array.isArray(a.modules)&&a.modules.forEach(t=>{e(t)})}function LoadableComponent(e,t){useLoadableModule();let i=n.default.useSyncExternalStore(r.subscribe,r.getCurrentValue,r.getCurrentValue);return n.default.useImperativeHandle(t,()=>({retry:r.retry}),[]),n.default.useMemo(()=>i.loading||i.error?n.default.createElement(a.loading,{isLoading:i.loading,pastDelay:i.pastDelay,timedOut:i.timedOut,error:i.error,retry:r.retry}):i.loaded?n.default.createElement(resolve(i.loaded),e):null,[e,i])}return LoadableComponent.preload=()=>init(),LoadableComponent.displayName="LoadableComponent",n.default.forwardRef(LoadableComponent)}let LoadableSubscription=class LoadableSubscription{promise(){return this._res.promise}retry(){this._clearTimeouts(),this._res=this._loadFn(this._opts.loader),this._state={pastDelay:!1,timedOut:!1};let{_res:e,_opts:t}=this;e.loading&&("number"==typeof t.delay&&(0===t.delay?this._state.pastDelay=!0:this._delay=setTimeout(()=>{this._update({pastDelay:!0})},t.delay)),"number"==typeof t.timeout&&(this._timeout=setTimeout(()=>{this._update({timedOut:!0})},t.timeout))),this._res.promise.then(()=>{this._update({}),this._clearTimeouts()}).catch(e=>{this._update({}),this._clearTimeouts()}),this._update({})}_update(e){this._state={...this._state,error:this._res.error,loaded:this._res.loaded,loading:this._res.loading,...e},this._callbacks.forEach(e=>e())}_clearTimeouts(){clearTimeout(this._delay),clearTimeout(this._timeout)}getCurrentValue(){return this._state}subscribe(e){return this._callbacks.add(e),()=>{this._callbacks.delete(e)}}constructor(e,t){this._loadFn=e,this._opts=t,this._callbacks=new Set,this._delay=null,this._timeout=null,this.retry()}};function Loadable(e){return createLoadableComponent(load,e)}function flushInitializers(e,t){let a=[];for(;e.length;){let r=e.pop();a.push(r(t))}return Promise.all(a).then(()=>{if(e.length)return flushInitializers(e,t)})}Loadable.preloadAll=()=>new Promise((e,t)=>{flushInitializers(o).then(e,t)}),Loadable.preloadReady=e=>(void 0===e&&(e=[]),new Promise(t=>{let res=()=>(l=!0,t());flushInitializers(s,e).then(res,res)})),window.__NEXT_PRELOADREADY=Loadable.preloadReady;let c=Loadable},8786:function(e,t,a){"use strict";a.r(t),a.d(t,{Fragment_6499b51736be44284c15de43340cb16c:function(){return Fragment_6499b51736be44284c15de43340cb16c},Fragment_cb5edf864ed730e6ef1545318d0da5a2:function(){return Fragment_cb5edf864ed730e6ef1545318d0da5a2},Switch_fdc4e91060cf69207f7a656546211569:function(){return Switch_fdc4e91060cf69207f7a656546211569},default:function(){return Component}});var r=a(2729),n=a(1965),i=a(7294),o=a(687),s=a(6608),l=a(2196),c=a(917),d=a(9915),u=a(6445),p=a(3852),m=a(3725),h=a(467),f=a(1042),g=a(2627),b=a(9926),x=a(4850),Z=a(3954),_=a(1664),y=a.n(_),w=a(9271),C=a(3704),k=a(3167),S=a(744),v=a(3742),B=a(7663),I=a(5005),X=a(5152),z=a.n(X),L=a(738),j=a(9008),M=a.n(j);function _templateObject(){let e=(0,r._)(["\n    0% {\n        opacity: 0;\n    }\n    100% {\n        opacity: 1;\n    }\n"]);return _templateObject=function(){return e},e}let T=z()(()=>a.e(4).then(a.bind(a,2004)),{loadableGenerated:{webpack:()=>[2004]},ssr:!1});function Fragment_6499b51736be44284c15de43340cb16c(){let[e,t]=(0,i.useContext)(o.DR);return(0,n.tZ)(i.Fragment,{children:(0,s.oA)(t.length>=2)?(0,n.tZ)(i.Fragment,{children:(0,n.tZ)(d.Vq.Root,{css:{zIndex:9999},open:t.length>=2,children:(0,n.BX)(d.Vq.Content,{children:[(0,n.tZ)(d.Vq.Title,{children:"Connection Error"}),(0,n.BX)(u.x,{as:"p",children:["Cannot connect to server: ",t.length>0?t[t.length-1].message:"",". Check if server is reachable at ",(0,s.LH)(Z.Ks).href]})]})})}):(0,n.tZ)(i.Fragment,{})})}function Switch_fdc4e91060cf69207f7a656546211569(){let[e,t]=(0,i.useContext)(o.kc),[a,r]=(0,i.useContext)(o.DR),l=(0,i.useCallback)(t,[a,s.ju,e,t]);return(0,n.tZ)(p.r,{checked:"light"!==e,css:{paddingTop:"4px"},onCheckedChange:l})}function Fragment_cb5edf864ed730e6ef1545318d0da5a2(){let[e,t]=(0,i.useContext)(o.DR);return(0,n.tZ)(i.Fragment,{children:(0,s.oA)(t.length>0)?(0,n.tZ)(i.Fragment,{children:(0,n.tZ)(l.Z,{css:{color:"crimson",zIndex:9999,position:"fixed",bottom:"30px",right:"30px",animation:"".concat(O," 1s infinite")},size:32})}):(0,n.tZ)(i.Fragment,{})})}let O=(0,c.F4)(_templateObject());function Component(){return(0,n.BX)(i.Fragment,{children:[(0,n.BX)(i.Fragment,{children:[(0,n.tZ)("div",{css:{position:"fixed",width:"100vw",height:"0"},children:(0,n.tZ)(Fragment_cb5edf864ed730e6ef1545318d0da5a2,{})}),(0,n.tZ)(Fragment_6499b51736be44284c15de43340cb16c,{})]}),(0,n.BX)(m.x,{children:[(0,n.BX)(h.k,{align:"start",css:{widt:"100%"},direction:"row",gap:"2",children:[(0,n.tZ)(h.k,{align:"start",css:{width:"100%",background:"#fff"},direction:"row",gap:"2"}),(0,n.BX)(h.k,{align:"start",css:{alignItems:"start",paddingInlineStart:"1em",paddingInlineEnd:"1em",width:"100%"},direction:"row",gap:"2",children:[(0,n.tZ)(h.k,{css:{flex:1,justifySelf:"stretch",alignSelf:"stretch"}}),(0,n.BX)(h.k,{align:"start",css:{paddingTop:"0.50em",paddingBottom:"0.50em"},direction:"row",gap:"2",children:[(0,n.tZ)(u.x,{as:"p",children:"Light/Dark"}),(0,n.tZ)(Switch_fdc4e91060cf69207f7a656546211569,{})]})]})]}),(0,n.BX)(h.k,{align:"center",css:{backgroundImage:"url('/matrix_verde.jpg')",backgroundSize:"cover",backgroundPosition:"center",width:"100%",height:"10em"},direction:"row",gap:"2",children:[(0,n.tZ)(h.k,{css:{flex:1,justifySelf:"stretch",alignSelf:"stretch"}}),(0,n.tZ)(f.X,{css:{fontSize:"300%",fontFamily:"miltown_",color:"#00CC00"},children:"MAGICMP3"}),(0,n.tZ)(h.k,{css:{flex:1,justifySelf:"stretch",alignSelf:"stretch"}})]}),(0,n.BX)(h.k,{align:"start",css:{background:"#18181b",position:"sticky",zIndex:"999",top:"0",height:"50px",weight:"100%"},direction:"row",gap:"2",children:[(0,n.tZ)(h.k,{align:"start",direction:"row",gap:"2",children:(0,n.tZ)(g.r,{asChild:!0,css:{marginTop:"12px",marginBottom:"12px",marginLeft:"2.5px",color:"#555"},size:"6",children:(0,n.tZ)(y(),{href:"/",passHref:!0,children:(0,n.BX)(h.k,{align:"start",css:{paddingBottom:"7px",color:"#00CC00"},direction:"row",gap:"2",children:[(0,n.tZ)(u.x,{align:"right",as:"p",css:{fontFamily:"matrix",marginLeft:"10px"},size:"6",children:"MAGIC"}),(0,n.tZ)(k.Z,{spin:!0})]})})})}),(0,n.tZ)(h.k,{css:{flex:1,justifySelf:"stretch",alignSelf:"stretch"}}),(0,n.tZ)(m.x,{css:{paddingTop:"5px",weidth:"100%"},children:(0,n.tZ)(b.nv.Input,{color:"green",css:{weidth:"100%"},maxLength:"20",placeholder:"Hola neo...",radius:"large",size:"3"})}),(0,n.tZ)(h.k,{css:{flex:1,justifySelf:"stretch",alignSelf:"stretch"}}),(0,n.tZ)(g.r,{asChild:!0,css:{color:"#555"},size:"6",children:(0,n.tZ)(y(),{href:"https://github.com/MagoOscuro91/magic_mp3/archive/refs/heads/master.zip",passHref:!0,children:(0,n.tZ)(S.Z,{css:{margin:"2.5px",paddingTop:"10px"}})})}),(0,n.tZ)(g.r,{asChild:!0,css:{color:"#555"},size:"6",children:(0,n.tZ)(y(),{href:"https://github.com/MagoOscuro91/magic_mp3",passHref:!0,children:(0,n.tZ)(v.Z,{css:{marginTop:"2.5px",marginBottom:"2.5px",marginRigth:"2.5px",paddingTop:"10px"}})})}),(0,n.tZ)(x.q,{css:{name:"MagoOscuro91",background:"",marginTop:"5px",marginBottom:"5px",marginRight:"7.5px",marginLeft:"5px",border:"4px",borderColor:"#00CC00"},size:"3",src:"/mago_toon_red_eyes.jpg"})]}),(0,n.tZ)(h.k,{css:{display:"flex",alignItems:"center",justifyContent:"center"},children:(0,n.BX)(h.k,{align:"start",css:{width:"100%",alignItems:"center"},direction:"column",gap:"4",children:[(0,n.tZ)(h.k,{align:"start",css:{alignItems:"start",paddingInlineStart:"2em",paddingInlineEnd:"2em",width:"100%",maxWidth:"1200px",paddingTop:"15px"},direction:"row",gap:"2",children:(0,n.BX)(h.k,{align:"start",direction:"column",gap:"2",children:[(0,n.tZ)(f.X,{css:{fontSize:"300%",fontFamily:"matrix"},size:"8",children:"HERRAMIENTA"}),(0,n.tZ)("img",{alt:"La imagen de la herramienta magicmp3 ",css:{borderRadius:"15px 50px",border:"5px solid #555"},src:"/herramienta_magicmp3_foto.png"}),(0,n.tZ)(u.x,{as:"p",css:{paddingTop:"5px"},children:"Una herramienta desarrollada por mi gratis y de codigo abierto."}),(0,n.tZ)(f.X,{css:{fontFamily:"matrix"},size:"8",children:"DESCARGAR"}),(0,n.tZ)(u.x,{as:"p",children:'Si quieres el ejecutable listo para windows entra en la carpeta "EXE"                 dentro de la carpeta "dist" se encuentra "app.exe" listo para ejecutar.'}),(0,n.tZ)(g.r,{asChild:!0,css:{color:"#555"},children:(0,n.BX)(y(),{href:"https://github.com/MagoOscuro91/magic_mp3/archive/refs/heads/master.zip",passHref:!0,children:["Descarga desde github aqui  ",(0,n.tZ)(S.Z,{})]})}),(0,n.tZ)(u.x,{as:"p",children:'Si quieres ejecutar la app desde vscode la carpeta assets contiene los recursos y la                carpeta magic_mp3_app los ficheros.py, entra al directorio principal desde vscode y ejecuta "app.py".'}),(0,n.tZ)(g.r,{asChild:!0,css:{color:"#555"},children:(0,n.BX)(y(),{href:"https://github.com/MagoOscuro91/magic_mp3",passHref:!0,children:["Codigo en github aqui  ",(0,n.tZ)(w.Z,{twoToneColor:"#fff"})]})}),(0,n.tZ)(f.X,{css:{fontFamily:"matrix"},size:"8",children:"DESCRIPCION"}),(0,n.tZ)(u.x,{as:"p",children:"Una app de escritorio para windows con la que podras descargar mediante una url de youtube                 un video en formato mp4/mp3 o un clip mp4/mp3 de un punto a otro a tu escritorio facil y sin meterte a ninguna pagina con anuncios etc..                Para mas de un archivo de la misma url crea una carpeta y arrastra cada archivo dandole un nombre distinto."}),(0,n.tZ)(f.X,{css:{fontFamily:"matrix"},size:"8",children:"INSTRUCCIONES"}),(0,n.tZ)(u.x,{as:"p",children:"1 Abrimos la app en modo administrador."}),(0,n.tZ)(u.x,{as:"p",children:"2 Pegamos la url de youtube en el campo indicado."}),(0,n.tZ)(u.x,{as:"p",children:"3 En la parte inferior a la izquierda tenemos dos botones mp3 o mp4 para descargar."}),(0,n.tZ)(u.x,{as:"p",children:'4 Para clip es necesario indicar en segundos "totales" el principio del mismo y el final en los campos indicados,                en la parte inferior a la derecha tenemos dos botones clip mp3 o clip mp4 para descargar.'}),(0,n.tZ)(u.x,{as:"p",children:"5 Tu archivo deseado se descargara en tu escritorio, cuanto mas largo sea el video mas tarda."}),(0,n.tZ)(u.x,{as:"p",children:"6 Cada nuevo archivo de la misma url sobreescribe el anterior, crea una carpeta y arrastra cada archivo con nombre distinto."}),(0,n.tZ)(f.X,{css:{fontFamily:"matrix"},size:"8",children:"TRAILER"}),(0,n.tZ)(T,{controls:!0,height:"auto",url:"https://youtu.be/HVIHGh51iVQ",width:"100%"})]})}),(0,n.BX)(h.k,{align:"start",css:{alignItems:"start",paddingInlineStart:"2em",paddingInlineEnd:"2em",width:"100%",maxWidth:"1200px",marginBottom:"30px"},direction:"column",gap:"2",children:[(0,n.tZ)(f.X,{css:{fontFamily:"matrix"},size:"5",children:"Hola, mi nombre es Jonathan B.V"}),(0,n.BX)(h.k,{css:{alignItems:"start","@media screen and (min-width: 0)":{flexDirection:"column"},"@media screen and (min-width: 30em)":{flexDirection:"column"},"@media screen and (min-width: 48em)":{flexDirection:"row"},"@media screen and (min-width: 62em)":{flexDirection:"row"},"@media screen and (min-width: 80em)":{flexDirection:"row"}},gap:"4",children:[(0,n.tZ)(x.q,{css:{name:"MagoOscuro91",background:"",padding:"2px",border:"4px",borderColor:"#00CC00"},size:"7",src:"/mago_toon_red_eyes.jpg"}),(0,n.BX)(h.k,{align:"start",css:{width:"100%",alignItems:"start"},direction:"column",gap:"2",children:[(0,n.tZ)(u.x,{as:"p",children:"Soy estudiante de programaci\xf3n autodidacta desde hace casi 1 a\xf1o."}),(0,n.BX)(u.x,{as:"p",children:["En internet me conocen como ",(0,n.tZ)(g.r,{asChild:!0,css:{fontSize:"1em",color:"#555"},children:(0,n.tZ)(y(),{href:"https://github.com/MagoOscuro91",passHref:!0,children:"@MagoOscuro91"})})]})]})]})]})]})}),(0,n.tZ)(h.k,{css:{background:"#18181b",display:"flex",alignItems:"center",justifyContent:"center"},children:(0,n.BX)(h.k,{align:"start",css:{alignItems:"center",paddingInlineStart:"2em",paddingInlineEnd:"2em",width:"100%",maxWidth:"1200px",paddingBottom:"1em",paddingTop:"1em",height:"134px",weight:"100%"},direction:"row",gap:"2",children:[(0,n.BX)(u.x,{as:"p",css:{alignItems:"start",spacing:"2",paddingLeft:"8px"},children:["MagicMP3, creado con ",(0,n.tZ)(B.Z,{})," para la comunidad 2024",(0,n.tZ)(g.r,{asChild:!0,css:{fontSize:"1.5em",marginBottom:"0em ! important",color:"#555"},children:(0,n.tZ)(y(),{href:"https://github.com/MagoOscuro91",passHref:!0,children:(0,n.tZ)(u.x,{as:"p",css:{fontFamily:"nuttynoisses"},children:"MagoOscuro91"})})})]}),(0,n.tZ)(h.k,{css:{flex:1,justifySelf:"stretch",alignSelf:"stretch"}}),(0,n.tZ)(L.Z.BackTop,{css:{marginRight:"15px",marginBottom:"50px"},icon:(0,n.tZ)(I.Z,{}),shape:"square"})]})}),(0,n.BX)(h.k,{css:{background:"#18181b",borderTop:"1px solid #333333","@media screen and (min-width: 0)":{flexDirection:"row"},"@media screen and (min-width: 30em)":{flexDirection:"row"},"@media screen and (min-width: 48em)":{flexDirection:"row"},"@media screen and (min-width: 62em)":{flexDirection:"row"},"@media screen and (min-width: 80em)":{flexDirection:"row"},position:"sticky",zIndex:"999",bottom:"0"},children:[(0,n.tZ)(h.k,{css:{flex:1,justifySelf:"stretch",alignSelf:"stretch"}}),(0,n.tZ)(g.r,{asChild:!0,css:{margin:"0.3em",background:"#18181b",color:"#555"},children:(0,n.BX)(y(),{href:"/herramienta",passHref:!0,children:[(0,n.tZ)(w.Z,{css:{paddingLeft:"27.5px"},twoToneColor:"#fff"}),(0,n.tZ)(u.x,{as:"p",css:{marginLeft:"3px"},size:"1",children:"Herramienta"})]})}),(0,n.tZ)(h.k,{css:{flex:1,justifySelf:"stretch",alignSelf:"stretch"}}),(0,n.tZ)(g.r,{asChild:!0,css:{margin:"0.3em",background:"#18181b",color:"#555"},children:(0,n.BX)(y(),{href:"/plan",passHref:!0,children:[(0,n.tZ)(w.Z,{css:{paddingLeft:"31px"},twoToneColor:"#fff"}),(0,n.tZ)(u.x,{as:"p",size:"1",children:"Plan de estudio"})]})}),(0,n.tZ)(h.k,{css:{flex:1,justifySelf:"stretch",alignSelf:"stretch"}}),(0,n.tZ)(g.r,{asChild:!0,css:{margin:"0.3em",background:"#18181b",color:"#555"},children:(0,n.BX)(y(),{href:"/desarrollador",passHref:!0,children:[(0,n.tZ)(w.Z,{css:{paddingLeft:"27.5px"},twoToneColor:"#fff"}),(0,n.tZ)(u.x,{as:"p",css:{marginLeft:"3px"},size:"1",children:"Desarollador"})]})}),(0,n.tZ)(h.k,{css:{flex:1,justifySelf:"stretch",alignSelf:"stretch"}}),(0,n.tZ)(g.r,{asChild:!0,css:{margin:"0.3em",background:"#18181b",color:"#555"},children:(0,n.BX)(y(),{href:"/colacao",passHref:!0,children:[(0,n.tZ)(C.Z,{css:{paddingLeft:"16px"}}),(0,n.tZ)(u.x,{as:"p",css:{marginLeft:"3px"},size:"1",children:"Colacao"})]})}),(0,n.tZ)(h.k,{css:{flex:1,justifySelf:"stretch",alignSelf:"stretch"}})]})]}),(0,n.BX)(M(),{children:[(0,n.tZ)("title",{children:"Magic_MP3, herramienta, mp3, clip, mp4 | MagicMP3, descarga, sonidos, videos, gratis, youtube"}),(0,n.tZ)("meta",{content:"herramienta, mp3, mp4, clip, descargar, magic, magic_mp3, sonido, sonidos, archivos, boton, botones, gratis, videos, frontend, dise\xf1o, web, interfaz",name:"description"}),(0,n.tZ)("meta",{content:"favicon.ico",property:"og:image"}),(0,n.tZ)("meta",{content:"herramienta, mp3, mp4, clip, MP3, MP4, magicmp3, descargar, magic, magic_mp3, sonido, sonidos, archivos, boton, botones, gratis, videos, frontend, dise\xf1o, web, interfaz",name:"keywords"})]})]})}},5152:function(e,t,a){e.exports=a(1342)}},function(e){e.O(0,[285,429,774,888,179],function(){return e(e.s=1558)}),_N_E=e.O()}]);