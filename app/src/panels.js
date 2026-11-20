export const layouts=[['classic','Classic Six'],['hero','Hero & Strips'],['triple','Triple Diagonal'],['quad','Quad Grid'],['full','Full Bleed']];
export function geometry(id){
 if(id==='full')return [[[0,0],[1,0],[1,1],[0,1]]];
 if(id==='quad')return [rect(0,0,.5,.5),rect(.5,0,1,.5),rect(0,.5,.5,1),rect(.5,.5,1,1)];
 if(id==='triple')return [[[0,0],[.41,0],[.25,1],[0,1]],[[.41,0],[.77,0],[.61,1],[.25,1]],[[.77,0],[1,0],[1,1],[.61,1]]];
 if(id==='hero')return [[[0,0],[.68,0],[.56,1],[0,1]],[[.68,0],[1,0],[1,.34],[.6392,.34]],[[.6392,.34],[1,.34],[1,.67],[.5996,.67]],[[.5996,.67],[1,.67],[1,1],[.56,1]]];
 return Array.from({length:6},(_,i)=>{const row=Math.floor(i/2),y=row/3,b=(row+1)/3,a=.54-row*.04,c=.54-(row+1)*.04;return i%2?[[a,y],[1,y],[1,b],[c,b]]:[[0,y],[a,y],[c,b],[0,b]]});
}
function rect(x,y,r,b){return [[x,y],[r,y],[r,b],[x,b]]}
export function path(ctx,points,w,h){ctx.beginPath();points.forEach(([x,y],i)=>i?ctx.lineTo(x*w,y*h):ctx.moveTo(x*w,y*h));ctx.closePath()}
export function bounds(p,w,h){const xs=p.map(v=>v[0]*w),ys=p.map(v=>v[1]*h);return {x:Math.min(...xs),y:Math.min(...ys),w:Math.max(...xs)-Math.min(...xs),h:Math.max(...ys)-Math.min(...ys)}}
export function contains(p,x,y){let inside=false;for(let i=0,j=p.length-1;i<p.length;j=i++){const a=p[i],b=p[j];if((a[1]>y)!=(b[1]>y)&&x<(b[0]-a[0])*(y-a[1])/(b[1]-a[1])+a[0])inside=!inside}return inside}
