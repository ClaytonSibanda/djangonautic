const titleinput = document.querySelector("input[nme=title]");
const sluginput = document.querySelector("input[nme=slug]");


const slugify =(val)=>{
  return val.toString().toLowerCase().trim().replace(/&/g,'-and-').replace(/[\s\W-]+/g,'-');
};
titleinput.addEventListener('keyup',(e)=>{
sluginput.setAttribute('value',slugify(titleinput.value))
});
