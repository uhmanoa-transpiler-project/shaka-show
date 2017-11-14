import { codeMirror } from './codemirror';

/**
 * Singleton class used for interaction with the SourceTracker panel.
 */
class SourceTracker {
  constructor(codeMirror) {
    this.codeMirror = codeMirror;
    this.files = {}
  }

  /**
   * Update the source code of any files in sourcetracker.
   * @param  {Object} changed_files contains keys=filenames and value=code
   */
  update(changed_files) {

  }

  /**
   * Store the current file displayed into the file object.
   */
  store() {

  }

  /**
   * Remove the given files from the file object.
   * @param {String} file to remove.
   */
  remove(file) {
    if(file in this.files) {
      delete this.files[file];
      // TODO: Remove the tab
      if(Object.keys(this.files).length) {
        this.display(Object.keys(this.files)[0]);
      }
    }
  }

  /**
   * Display the given file in the CodeMirror.
   * @param {String} file The name of the file to display.
   */
  display(file) {
    this.store();
    this.codeMirror.setValue(this.files[file]);
  }
}

export const sourceTracker = new SourceTracker(codeMirror);