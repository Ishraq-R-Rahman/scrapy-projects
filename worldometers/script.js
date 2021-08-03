const exec = require('child_process').exec
const path = require('path')

const file_path = path.join(__dirname, '/run.py')
exec( 'python ' + file_path, function(err,stdout,stderr){
    if( err ){
        console.log(stderr);
        return;
    }
    console.log(`stdout: ${stdout}`);
    console.error(`stderr: ${stderr}`);
} )