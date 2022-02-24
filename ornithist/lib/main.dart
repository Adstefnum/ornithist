import 'package:flutter/material.dart';
import 'package:path_provider/path_provider.dart';
import 'package:image_picker/image_picker.dart';
import 'package:path/path.dart';
import 'package:http/http.dart' as http;
import 'package:camera/camera.dart';

void main() {
	runApp(PhotoPreviewScreen());
}

class PhotoPreviewScreen extends StatefulWidget {
  @override
  _PhotoPreviewScreenState createState() => _PhotoPreviewScreenState();
}
 
class _PhotoPreviewScreenState extends State<PhotoPreviewScreen> {
  var imageFile;
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: Column(
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
_openGallery(context);

},

),
Padding(padding:EdgeInsets.all(0.0)),

GestureDetector(
child: Text("Camera"),
onTap: (){
_openCamera(context);
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

      return Image.file(imageFile, width: 500, height: 500);

    } else {

      return Text("Please select an image");

    }

  }

void _openGallery(BuildContext context) async {
    var picture = await ImagePicker().pickImage(source: ImageSource.gallery);

    this.setState(() {

      imageFile = picture;

    });

    Navigator.of(context).pop();

  }


void _openCamera(BuildContext context) async{
    var picture = await ImagePicker().pickImage(source: ImageSource.camera);

    this.setState(() {

      imageFile = picture;

    });

    Navigator.of(context).pop();
}
}
