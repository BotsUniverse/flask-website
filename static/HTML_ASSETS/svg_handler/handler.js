class Dict extends Object {
  constructor ( object = {} )
  {
    super( object );
    this.object = object;
    
  }
  values () {

  }
}



class SVGHandler {

  constructor (objects = {}) {
    this.parent_attributes = objects;
    this.parent_element = document.createElement('svg');
  }

}