(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[152],{1558:function(e,t,n){(window.__NEXT_P=window.__NEXT_P||[]).push(["/herramienta",function(){return n(8786)}])},1342:function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),function(e,t){for(var n in t)Object.defineProperty(e,n,{enumerable:!0,get:t[n]})}(t,{noSSR:function(){return noSSR},default:function(){return dynamic}});let a=n(8754),i=(n(7294),a._(n(4304)));function convertModule(e){return{default:(null==e?void 0:e.default)||e}}function noSSR(e,t){return delete t.webpack,delete t.modules,e(t)}function dynamic(e,t){let n=i.default,a={loading:e=>{let{error:t,isLoading:n,pastDelay:a}=e;return null}};e instanceof Promise?a.loader=()=>e:"function"==typeof e?a.loader=e:"object"==typeof e&&(a={...a,...e}),a={...a,...t};let r=a.loader;return(a.loadableGenerated&&(a={...a,...a.loadableGenerated},delete a.loadableGenerated),"boolean"!=typeof a.ssr||a.ssr)?n({...a,loader:()=>null!=r?r().then(convertModule):Promise.resolve(convertModule(()=>null))}):(delete a.webpack,delete a.modules,noSSR(n,a))}("function"==typeof t.default||"object"==typeof t.default&&null!==t.default)&&void 0===t.default.__esModule&&(Object.defineProperty(t.default,"__esModule",{value:!0}),Object.assign(t.default,t),e.exports=t.default)},43:function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0}),Object.defineProperty(t,"LoadableContext",{enumerable:!0,get:function(){return r}});let a=n(8754),i=a._(n(7294)),r=i.default.createContext(null)},4304:function(e,t,n){"use strict";/**
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
*/Object.defineProperty(t,"__esModule",{value:!0}),Object.defineProperty(t,"default",{enumerable:!0,get:function(){return c}});let a=n(8754),i=a._(n(7294)),r=n(43);function resolve(e){return e&&e.default?e.default:e}let o=[],s=[],d=!1;function load(e){let t=e(),n={loading:!0,loaded:null,error:null};return n.promise=t.then(e=>(n.loading=!1,n.loaded=e,e)).catch(e=>{throw n.loading=!1,n.error=e,e}),n}function createLoadableComponent(e,t){let n=Object.assign({loader:null,loading:null,delay:200,timeout:null,webpack:null,modules:null},t),a=null;function init(){if(!a){let t=new LoadableSubscription(e,n);a={getCurrentValue:t.getCurrentValue.bind(t),subscribe:t.subscribe.bind(t),retry:t.retry.bind(t),promise:t.promise.bind(t)}}return a.promise()}if(!d){let e=n.webpack?n.webpack():n.modules;e&&s.push(t=>{for(let n of e)if(t.includes(n))return init()})}function useLoadableModule(){init();let e=i.default.useContext(r.LoadableContext);e&&Array.isArray(n.modules)&&n.modules.forEach(t=>{e(t)})}function LoadableComponent(e,t){useLoadableModule();let r=i.default.useSyncExternalStore(a.subscribe,a.getCurrentValue,a.getCurrentValue);return i.default.useImperativeHandle(t,()=>({retry:a.retry}),[]),i.default.useMemo(()=>r.loading||r.error?i.default.createElement(n.loading,{isLoading:r.loading,pastDelay:r.pastDelay,timedOut:r.timedOut,error:r.error,retry:a.retry}):r.loaded?i.default.createElement(resolve(r.loaded),e):null,[e,r])}return LoadableComponent.preload=()=>init(),LoadableComponent.displayName="LoadableComponent",i.default.forwardRef(LoadableComponent)}let LoadableSubscription=class LoadableSubscription{promise(){return this._res.promise}retry(){this._clearTimeouts(),this._res=this._loadFn(this._opts.loader),this._state={pastDelay:!1,timedOut:!1};let{_res:e,_opts:t}=this;e.loading&&("number"==typeof t.delay&&(0===t.delay?this._state.pastDelay=!0:this._delay=setTimeout(()=>{this._update({pastDelay:!0})},t.delay)),"number"==typeof t.timeout&&(this._timeout=setTimeout(()=>{this._update({timedOut:!0})},t.timeout))),this._res.promise.then(()=>{this._update({}),this._clearTimeouts()}).catch(e=>{this._update({}),this._clearTimeouts()}),this._update({})}_update(e){this._state={...this._state,error:this._res.error,loaded:this._res.loaded,loading:this._res.loading,...e},this._callbacks.forEach(e=>e())}_clearTimeouts(){clearTimeout(this._delay),clearTimeout(this._timeout)}getCurrentValue(){return this._state}subscribe(e){return this._callbacks.add(e),()=>{this._callbacks.delete(e)}}constructor(e,t){this._loadFn=e,this._opts=t,this._callbacks=new Set,this._delay=null,this._timeout=null,this.retry()}};function Loadable(e){return createLoadableComponent(load,e)}function flushInitializers(e,t){let n=[];for(;e.length;){let a=e.pop();n.push(a(t))}return Promise.all(n).then(()=>{if(e.length)return flushInitializers(e,t)})}Loadable.preloadAll=()=>new Promise((e,t)=>{flushInitializers(o).then(e,t)}),Loadable.preloadReady=e=>(void 0===e&&(e=[]),new Promise(t=>{let res=()=>(d=!0,t());flushInitializers(s,e).then(res,res)})),window.__NEXT_PRELOADREADY=Loadable.preloadReady;let c=Loadable},8786:function(e,t,n){"use strict";n.r(t),n.d(t,{Fragment_6499b51736be44284c15de43340cb16c:function(){return Fragment_6499b51736be44284c15de43340cb16c},Fragment_cb5edf864ed730e6ef1545318d0da5a2:function(){return Fragment_cb5edf864ed730e6ef1545318d0da5a2},Link_0451e1d44e99ecef448e050ea1fe2fbe:function(){return Link_0451e1d44e99ecef448e050ea1fe2fbe},Link_7142dda7d6cbf21f43e5929d71a152e8:function(){return Link_7142dda7d6cbf21f43e5929d71a152e8},Link_9410e4946328ea31b571d8d572dc5743:function(){return Link_9410e4946328ea31b571d8d572dc5743},Link_f46ea07de44e8594fc6e837e7901ae6b:function(){return Link_f46ea07de44e8594fc6e837e7901ae6b},Switch_fdc4e91060cf69207f7a656546211569:function(){return Switch_fdc4e91060cf69207f7a656546211569},default:function(){return Component}});var a=n(2729),i=n(1965),r=n(7294),o=n(687),s=n(6608),d=n(2196),c=n(917),l=n(2627),p=n(3852),u=n(9915),m=n(6445),f=n(3725),h=n(467),g=n(1042),b=n(9926),x=n(4850),_=n(3954),Z=n(1664),y=n.n(Z),k=n(9271),w=n(3704),C=n(3167),S=n(744),L=n(3742),T=n(7663),B=n(5005),I=n(5152),v=n.n(I),X=n(738),j=n(9008),z=n.n(j);function _templateObject(){let e=(0,a._)(["\n    0% {\n        opacity: 0;\n    }\n    100% {\n        opacity: 1;\n    }\n"]);return _templateObject=function(){return e},e}let M=v()(()=>n.e(4).then(n.bind(n,2004)),{loadableGenerated:{webpack:()=>[2004]},ssr:!1});function Link_9410e4946328ea31b571d8d572dc5743(){return(0,i.tZ)(l.r,{asChild:!0,css:{color:"#555"},size:"6",target:(0,s.oA)(!0)?"_blank":"",children:(0,i.tZ)(y(),{href:"https://github.com/MagoOscuro91/Magic_MP3_web",passHref:!0,children:(0,i.tZ)(L.Z,{css:{marginTop:"2.5px",marginBottom:"2.5px",marginRigth:"2.5px",paddingTop:"11px"}})})})}function Link_0451e1d44e99ecef448e050ea1fe2fbe(){return(0,i.tZ)(l.r,{asChild:!0,css:{color:"#555"},size:"7",target:(0,s.oA)(!0)?"_blank":"",children:(0,i.tZ)(y(),{href:"https://github.com/MagoOscuro91/magic_mp3",passHref:!0,children:(0,i.tZ)(S.Z,{css:{marginTop:"2.5px",marginBottom:"2.5px",marginRigt:"2.5px",paddingTop:"10px"}})})})}function Link_f46ea07de44e8594fc6e837e7901ae6b(){return(0,i.tZ)(l.r,{asChild:!0,css:{fontSize:"1em",color:"#555"},target:(0,s.oA)(!0)?"_blank":"",children:(0,i.tZ)(y(),{href:"https://www.youtube.com/channel/UCSreSq8_KxuME4T7aQlgQHw",passHref:!0,children:"@MagoOscuro91"})})}function Fragment_cb5edf864ed730e6ef1545318d0da5a2(){let[e,t]=(0,r.useContext)(o.DR);return(0,i.tZ)(r.Fragment,{children:(0,s.oA)(t.length>0)?(0,i.tZ)(r.Fragment,{children:(0,i.tZ)(d.Z,{css:{color:"crimson",zIndex:9999,position:"fixed",bottom:"30px",right:"30px",animation:"".concat(O," 1s infinite")},size:32})}):(0,i.tZ)(r.Fragment,{})})}let O=(0,c.F4)(_templateObject());function Link_7142dda7d6cbf21f43e5929d71a152e8(){return(0,i.tZ)(l.r,{asChild:!0,css:{color:"#555"},target:(0,s.oA)(!0)?"_blank":"",children:(0,i.BX)(y(),{href:"https://github.com/MagoOscuro91/magic_mp3",passHref:!0,children:["C\xf3digo en GitHub aqu\xed  ",(0,i.tZ)(k.Z,{twoToneColor:"#fff"})]})})}function Switch_fdc4e91060cf69207f7a656546211569(){let[e,t]=(0,r.useContext)(o.kc),[n,a]=(0,r.useContext)(o.DR),d=(0,r.useCallback)(t,[n,s.ju,e,t]);return(0,i.tZ)(p.r,{checked:"light"!==e,css:{paddingTop:"4px"},onCheckedChange:d})}function Fragment_6499b51736be44284c15de43340cb16c(){let[e,t]=(0,r.useContext)(o.DR);return(0,i.tZ)(r.Fragment,{children:(0,s.oA)(t.length>=2)?(0,i.tZ)(r.Fragment,{children:(0,i.tZ)(u.Vq.Root,{css:{zIndex:9999},open:t.length>=2,children:(0,i.BX)(u.Vq.Content,{children:[(0,i.tZ)(u.Vq.Title,{children:"Connection Error"}),(0,i.BX)(m.x,{as:"p",children:["Cannot connect to server: ",t.length>0?t[t.length-1].message:"",". Check if server is reachable at ",(0,s.LH)(_.Ks).href]})]})})}):(0,i.tZ)(r.Fragment,{})})}function Component(){return(0,i.BX)(r.Fragment,{children:[(0,i.BX)(r.Fragment,{children:[(0,i.tZ)("div",{css:{position:"fixed",width:"100vw",height:"0"},children:(0,i.tZ)(Fragment_cb5edf864ed730e6ef1545318d0da5a2,{})}),(0,i.tZ)(Fragment_6499b51736be44284c15de43340cb16c,{})]}),(0,i.BX)(f.x,{children:[(0,i.BX)(h.k,{align:"start",css:{widt:"100%"},direction:"row",gap:"2",children:[(0,i.tZ)(h.k,{align:"start",css:{width:"100%",background:"#fff"},direction:"row",gap:"2"}),(0,i.BX)(h.k,{align:"start",css:{alignItems:"start",paddingInlineStart:"1em",paddingInlineEnd:"1em",width:"100%"},direction:"row",gap:"2",children:[(0,i.tZ)(h.k,{css:{flex:1,justifySelf:"stretch",alignSelf:"stretch"}}),(0,i.BX)(h.k,{align:"start",css:{paddingTop:"0.50em",paddingBottom:"0.50em"},direction:"row",gap:"2",children:[(0,i.tZ)(m.x,{as:"p",children:"Light/Dark"}),(0,i.tZ)(Switch_fdc4e91060cf69207f7a656546211569,{})]})]})]}),(0,i.BX)(h.k,{align:"center",css:{backgroundImage:"url('/matrix_verde.jpg')",backgroundSize:"cover",backgroundPosition:"center",width:"100%",height:"10em"},direction:"row",gap:"2",children:[(0,i.tZ)(h.k,{css:{flex:1,justifySelf:"stretch",alignSelf:"stretch"}}),(0,i.tZ)(g.X,{css:{fontSize:"300%",fontFamily:"miltown_",color:"#00CC00"},children:"MAGICMP3"}),(0,i.tZ)(h.k,{css:{flex:1,justifySelf:"stretch",alignSelf:"stretch"}})]}),(0,i.BX)(h.k,{align:"start",css:{background:"#18181b",position:"sticky",zIndex:"999",top:"0",height:"50px",weight:"100%"},direction:"row",gap:"2",children:[(0,i.tZ)(h.k,{align:"start",direction:"row",gap:"2",children:(0,i.tZ)(l.r,{asChild:!0,css:{marginTop:"12px",marginBottom:"12px",marginLeft:"2.5px",color:"#555"},size:"6",children:(0,i.tZ)(y(),{href:"/",passHref:!0,children:(0,i.BX)(h.k,{align:"start",css:{paddingBottom:"7px",color:"#00CC00"},direction:"row",gap:"2",children:[(0,i.tZ)(m.x,{align:"right",as:"p",css:{fontFamily:"matrix",marginLeft:"10px"},size:"6",children:"MAGIC"}),(0,i.tZ)(C.Z,{spin:!0})]})})})}),(0,i.tZ)(h.k,{css:{flex:1,justifySelf:"stretch",alignSelf:"stretch"}}),(0,i.tZ)(f.x,{css:{paddingTop:"5px",marginLeft:"10px",weidth:"100%"},children:(0,i.tZ)(b.nv.Input,{color:"green",css:{weidth:"100%"},maxLength:"20",placeholder:"Hola Neo...",radius:"large",size:"3"})}),(0,i.tZ)(h.k,{css:{flex:1,justifySelf:"stretch",alignSelf:"stretch"}}),(0,i.tZ)(Link_0451e1d44e99ecef448e050ea1fe2fbe,{}),(0,i.tZ)(Link_9410e4946328ea31b571d8d572dc5743,{}),(0,i.tZ)(x.q,{css:{name:"MagoOscuro91",background:"",marginTop:"5px",marginBottom:"5px",marginRight:"5px",marginLeft:"5px",border:"4px",borderColor:"#00CC00"},size:"3",src:"/mago_toon_red_eyes.jpg"})]}),(0,i.tZ)(h.k,{css:{display:"flex",alignItems:"center",justifyContent:"center"},children:(0,i.BX)(h.k,{align:"start",css:{width:"100%",alignItems:"center"},direction:"column",gap:"4",children:[(0,i.BX)(h.k,{align:"start",css:{alignItems:"center",paddingInlineStart:"2em",paddingInlineEnd:"2em",width:"100%",maxWidth:"1200px"},direction:"column",gap:"2",children:[(0,i.tZ)(h.k,{css:{weidth:"100%",flex:1,justifySelf:"stretch",alignSelf:"stretch"}}),(0,i.tZ)(g.X,{css:{fontSize:"300%",marginTop:"35px",fontFamily:"matrix"},size:"8",children:"HERRAMIENTA"}),(0,i.tZ)("img",{alt:"La imagen de la herramienta magic mp3",css:{borderRadius:"15px 50px",border:"5px solid #555",width:"85%",height:"auto",marginTop:"35px",marginBottom:"10px"},src:"/herramienta_magicmp3_foto.png"}),(0,i.tZ)(m.x,{as:"p",css:{paddingTop:"5px"},children:"Una herramienta desarrollada por mi gratis y de c\xf3digo abierto."}),(0,i.tZ)(h.k,{css:{weidth:"100%",flex:1,justifySelf:"stretch",alignSelf:"stretch"}})]}),(0,i.tZ)(h.k,{align:"start",css:{alignItems:"start",paddingInlineStart:"2em",paddingInlineEnd:"2em",width:"100%",maxWidth:"1200px",paddingTop:"15px"},direction:"row",gap:"2",children:(0,i.BX)(h.k,{align:"start",direction:"column",gap:"2",children:[(0,i.tZ)(g.X,{css:{fontFamily:"matrix"},size:"8",children:"DESCARGAR"}),(0,i.tZ)(m.x,{as:"p",children:'Si quieres el ejecutable listo para Windows entra en la carpeta "EXE"                 dentro de la carpeta "dist" se encuentra "app.exe" listo para ejecutar.'}),(0,i.tZ)(l.r,{asChild:!0,css:{color:"#555"},children:(0,i.BX)(y(),{href:"https://github.com/MagoOscuro91/magic_mp3/archive/refs/heads/master.zip",passHref:!0,children:["Descarga desde GitHub aqu\xed  ",(0,i.tZ)(S.Z,{})]})}),(0,i.tZ)(m.x,{as:"p",children:'Si quieres ejecutar la app desde vscode la carpeta assets contiene los recursos y la                carpeta magic_mp3_app los ficheros.py, entra al directorio principal desde VScode y ejecuta "app.py".'}),(0,i.tZ)(Link_7142dda7d6cbf21f43e5929d71a152e8,{}),(0,i.tZ)(g.X,{css:{marginTop:"25px",fontFamily:"matrix"},size:"8",children:"DESCRIPCION"}),(0,i.tZ)(m.x,{as:"p",children:"Una app de escritorio para Windows con la que podr\xe1s descargar mediante una URL de YouTube                 un video en formato mp4/mp3 o un clip mp4/mp3 de un punto a otro a tu escritorio f\xe1cil y sin meterte a ninguna p\xe1gina con anuncios, etc...                Para m\xe1s de un archivo de la misma URL, crea una carpeta y arrastra cada archivo d\xe1ndole un nombre distinto."}),(0,i.tZ)(g.X,{css:{marginTop:"25px",fontFamily:"matrix"},size:"8",children:"INSTRUCCIONES"}),(0,i.tZ)(m.x,{as:"p",children:"1 Abrimos la app en modo administrador."}),(0,i.tZ)(m.x,{as:"p",children:"2 Pegamos la URL de YouTube en el campo indicado."}),(0,i.tZ)(m.x,{as:"p",children:"3 En la parte inferior a la izquierda tenemos dos botones mp3 o mp4 para descargar."}),(0,i.tZ)(m.x,{as:"p",children:'4 Para clip es necesario indicar en segundos "totales" el principio del mismo y el final en los campos indicados,                en la parte inferior a la derecha tenemos dos botones clip mp3 o clip mp4 para descargar.'}),(0,i.tZ)(m.x,{as:"p",children:"5 Tu archivo deseado se descargara en tu escritorio, cuanto m\xe1s largo sea el video m\xe1s tarda."}),(0,i.tZ)(m.x,{as:"p",children:"6 Cada nuevo archivo de la misma URL sobreescribe el anterior, crea una carpeta y arrastra cada archivo con nombre distinto."}),(0,i.tZ)(g.X,{css:{marginTop:"25px",fontFamily:"matrix"},size:"8",children:"TUTORIAL"}),(0,i.tZ)(M,{controls:!0,css:{marginBottom:"25px"},height:"auto",url:"https://youtu.be/oIgieqU4D9U",width:"100%"})]})}),(0,i.BX)(h.k,{align:"start",css:{alignItems:"start",paddingInlineStart:"2em",paddingInlineEnd:"2em",width:"100%",maxWidth:"1200px",marginBottom:"30px",marginTop:"15px"},direction:"column",gap:"2",children:[(0,i.tZ)(g.X,{css:{fontFamily:"matrix"},size:"5",children:"Hola, mi nombre es Jonathan B.V"}),(0,i.BX)(h.k,{css:{alignItems:"start","@media screen and (min-width: 0)":{flexDirection:"column"},"@media screen and (min-width: 30em)":{flexDirection:"column"},"@media screen and (min-width: 48em)":{flexDirection:"row"},"@media screen and (min-width: 62em)":{flexDirection:"row"},"@media screen and (min-width: 80em)":{flexDirection:"row"}},gap:"4",children:[(0,i.tZ)(x.q,{css:{name:"MagoOscuro91",background:"",padding:"2px",border:"4px",borderColor:"#00CC00"},size:"7",src:"/mago_toon_red_eyes.jpg"}),(0,i.BX)(h.k,{align:"start",css:{width:"100%",alignItems:"start"},direction:"column",gap:"2",children:[(0,i.tZ)(m.x,{as:"p",children:"Soy estudiante de programaci\xf3n autodidacta desde hace casi 1 a\xf1o."}),(0,i.BX)(m.x,{as:"p",children:["En internet me conocen como ",(0,i.tZ)(Link_f46ea07de44e8594fc6e837e7901ae6b,{})]})]})]})]})]})}),(0,i.tZ)(h.k,{css:{background:"#18181b",display:"flex",alignItems:"center",justifyContent:"center"},children:(0,i.BX)(h.k,{align:"start",css:{alignItems:"center",paddingInlineStart:"2em",paddingInlineEnd:"2em",width:"100%",maxWidth:"1200px",paddingBottom:"1em",paddingTop:"1em",height:"134px",weight:"100%"},direction:"row",gap:"2",children:[(0,i.BX)(m.x,{as:"p",css:{alignItems:"start",spacing:"2",paddingLeft:"8px"},children:["MagicMP3, creado con ",(0,i.tZ)(T.Z,{})," para la comunidad 2024",(0,i.tZ)(l.r,{asChild:!0,css:{fontSize:"1.5em",marginBottom:"0em ! important",color:"#555"},children:(0,i.tZ)(y(),{href:"https://github.com/MagoOscuro91",passHref:!0,children:(0,i.tZ)(m.x,{as:"p",css:{fontFamily:"nuttynoisses"},children:"MagoOscuro91"})})})]}),(0,i.tZ)(h.k,{css:{flex:1,justifySelf:"stretch",alignSelf:"stretch"}}),(0,i.tZ)(X.Z.BackTop,{css:{marginRight:"15px",marginBottom:"50px"},icon:(0,i.tZ)(B.Z,{}),shape:"square"})]})}),(0,i.BX)(h.k,{css:{background:"#18181b",borderTop:"1px solid #333333","@media screen and (min-width: 0)":{flexDirection:"row"},"@media screen and (min-width: 30em)":{flexDirection:"row"},"@media screen and (min-width: 48em)":{flexDirection:"row"},"@media screen and (min-width: 62em)":{flexDirection:"row"},"@media screen and (min-width: 80em)":{flexDirection:"row"},position:"sticky",zIndex:"999",bottom:"0"},children:[(0,i.tZ)(h.k,{css:{flex:1,justifySelf:"stretch",alignSelf:"stretch"}}),(0,i.tZ)(l.r,{asChild:!0,css:{margin:"0.3em",background:"#18181b",color:"#555"},children:(0,i.BX)(y(),{href:"/herramienta",passHref:!0,children:[(0,i.tZ)(k.Z,{css:{paddingLeft:"27.5px"},twoToneColor:"#fff"}),(0,i.tZ)(m.x,{as:"p",css:{marginLeft:"3px"},size:"1",children:"Herramienta"})]})}),(0,i.tZ)(h.k,{css:{flex:1,justifySelf:"stretch",alignSelf:"stretch"}}),(0,i.tZ)(l.r,{asChild:!0,css:{margin:"0.3em",background:"#18181b",color:"#555"},children:(0,i.BX)(y(),{href:"/plan",passHref:!0,children:[(0,i.tZ)(k.Z,{css:{paddingLeft:"31px"},twoToneColor:"#fff"}),(0,i.tZ)(m.x,{as:"p",size:"1",children:"Plan de estudio"})]})}),(0,i.tZ)(h.k,{css:{flex:1,justifySelf:"stretch",alignSelf:"stretch"}}),(0,i.tZ)(l.r,{asChild:!0,css:{margin:"0.3em",background:"#18181b",color:"#555"},children:(0,i.BX)(y(),{href:"/desarrollador",passHref:!0,children:[(0,i.tZ)(k.Z,{css:{paddingLeft:"27.5px"},twoToneColor:"#fff"}),(0,i.tZ)(m.x,{as:"p",css:{marginLeft:"3px"},size:"1",children:"Desarollador"})]})}),(0,i.tZ)(h.k,{css:{flex:1,justifySelf:"stretch",alignSelf:"stretch"}}),(0,i.tZ)(l.r,{asChild:!0,css:{margin:"0.3em",background:"#18181b",color:"#555"},children:(0,i.BX)(y(),{href:"/colacao",passHref:!0,children:[(0,i.tZ)(w.Z,{css:{paddingLeft:"16px"}}),(0,i.tZ)(m.x,{as:"p",css:{marginLeft:"3px"},size:"1",children:"Colacao"})]})}),(0,i.tZ)(h.k,{css:{flex:1,justifySelf:"stretch",alignSelf:"stretch"}})]})]}),(0,i.BX)(z(),{children:[(0,i.tZ)("title",{children:"Magic_MP3, herramienta, mp3, clip, mp4 | MagicMP3, descarga, sonidos, videos, gratis, youtube"}),(0,i.tZ)("meta",{content:"herramienta, mp3, mp4, clip, descargar, magic, magic_mp3, sonido, sonidos, archivos, boton, botones, gratis, videos, frontend, dise\xf1o, web, interfaz",name:"description"}),(0,i.tZ)("meta",{content:"favicon.ico",property:"og:image"}),(0,i.tZ)("meta",{content:"herramienta, mp3, mp4, clip, MP3, MP4, magicmp3, descargar, magic, magic_mp3, sonido, sonidos, archivos, boton, botones, gratis, videos, frontend, dise\xf1o, web, interfaz",name:"keywords"})]})]})}},5152:function(e,t,n){e.exports=n(1342)}},function(e){e.O(0,[285,429,774,888,179],function(){return e(e.s=1558)}),_N_E=e.O()}]);