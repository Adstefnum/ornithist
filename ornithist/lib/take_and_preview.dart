import  'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import 'dart:async';
import 'dart:io';

class PhotoPreviewScreen extends StatefulWidget {
        @override
  _PhotoPreviewScreenState createState() => _PhotoPreviewScreenState();
}
 
class _PhotoPreviewScreenState extends State<PhotoPreviewScreen> {
  File imageFile;
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
    backgroundColor: Colors.lightGreen,
    title: Text("Ornithist"),
    ),
      body: Center(

        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,       
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            _setImageView(imageFile)
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          _showSelectionDialog(context);
        },
        child: Icon(Icons.camera_alt),
        backgroundColor: Colors.black,
      ),
    );
  }

Future<void> _showSelectionDialog(BuildContext context){
	return showDialog(
    context:context,
			builder: (BuildContext context){
			return AlertDialog(
					title: Text("Choose Image Location"),
					content: SingleChildScrollView(
						child:ListBody(
							children: <Widget>[
							GestureDetector(
								child: Text("Gallery"),
onTap: (){
_selectImage(context,ImageSource.gallery);

},

),
Padding(padding:EdgeInsets.all(15.0)),

GestureDetector(
child: Text("Camera"),
onTap: (){
_selectImage(context,ImageSource.camera);
},
),
							]
							)
						)
					);
			}
			);
	}
Widget _setImageView(imageFile) {

    if (imageFile != null) {

      return Image.file(imageFile,
                      scale:1.0);

    } else {

      return Center(child:Text("Please select an image"));

    }

  }

void _selectImage(BuildContext context, ImageSource source) async {
    final XFile picture = await ImagePicker().pickImage(source: source);

    final File file = File(picture.path);

    this.setState(() {

      imageFile = file;

    });

    Navigator.of(context).pop();

  }

}

