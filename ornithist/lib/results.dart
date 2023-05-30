import '/flutter_flow/flutter_flow_icon_button.dart';
import '/flutter_flow/flutter_flow_theme.dart';
import '/flutter_flow/flutter_flow_util.dart';
import 'package:expandable/expandable.dart';
import 'package:flutter/material.dart';

import 'results_model.dart';
export 'results_model.dart';

class ResultsWidget extends StatefulWidget {
  const ResultsWidget({
    Key? key,
    String? imgPath,
    String? title,
    required this.desc,
  })  : this.imgPath = imgPath ??
            'https://t4.ftcdn.net/jpg/01/77/47/67/360_F_177476718_VWfYMWCzK32bfPI308wZljGHvAUYSJcn.jpg',
        this.title = title ?? 'Bird Name',
        super(key: key);

  final String imgPath;
  final String title;
  final String? desc;

  @override
  _ResultsWidgetState createState() => _ResultsWidgetState();
}

class _ResultsWidgetState extends State<ResultsWidget> {
  late ResultsModel _model;

  final scaffoldKey = GlobalKey<ScaffoldState>();
  final _unfocusNode = FocusNode();

  @override
  void initState() {
    super.initState();
    _model = createModel(context, () => ResultsModel());
  }

  @override
  void dispose() {
    _model.dispose();

    _unfocusNode.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: () => FocusScope.of(context).requestFocus(_unfocusNode),
      child: Scaffold(
        key: scaffoldKey,
        backgroundColor: Theme.of(context).secondaryBackground,
        appBar: AppBar(
          backgroundColor: Theme.of(context).primary,
          automaticallyImplyLeading: false,
          leading: IconButton(
            borderColor: Colors.transparent,
            borderRadius: 30,
            borderWidth: 1,
            buttonSize: 60,
            icon: Icon(
              Icons.arrow_back_rounded,
              color: Theme.of(context).primaryText,
              size: 30,
            ),
            onPressed: () async {
              context.pushNamed('HomePage');
            },
          ),
          actions: [],
          flexibleSpace: FlexibleSpaceBar(
            background: Container(),
          ),
          centerTitle: true,
          elevation: 0,
        ),
        body: SafeArea(
          top: true,
          child: Column(
            mainAxisSize: MainAxisSize.max,
            children: [
              Expanded(
                child: SingleChildScrollView(
                  child: Column(
                    mainAxisSize: MainAxisSize.max,
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Padding(
                        padding: EdgeInsetsDirectional.fromSTEB(16, 0, 16, 0),
                        child: Column(
                          mainAxisSize: MainAxisSize.max,
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            Padding(
                              padding:
                                  EdgeInsetsDirectional.fromSTEB(0, 16, 0, 0),
                              child: Container(
                                width: double.infinity,
                                height: 230,
                                decoration: BoxDecoration(
                                  color: Theme.of(context).alternate,
                                  boxShadow: [
                                    BoxShadow(
                                      blurRadius: 12,
                                      color: Color(0x33000000),
                                      offset: Offset(0, 5),
                                    )
                                  ],
                                  borderRadius: BorderRadius.circular(12),
                                ),
                                child: Padding(
                                  padding: EdgeInsetsDirectional.fromSTEB(
                                      2, 2, 2, 2),
                                  child: ClipRRect(
                                    borderRadius: BorderRadius.circular(10),
                                    child: Image.network(
                                      widget.imgPath,
                                      width: double.infinity,
                                      height: 230,
                                      fit: BoxFit.cover,
                                    ),
                                  ),
                                ),
                              ),
                            ),
                          ],
                        ),
                      ),
                      Padding(
                        padding: EdgeInsetsDirectional.fromSTEB(16, 0, 16, 0),
                        child: Container(
                          width: double.infinity,
                          color:
                              Theme.of(context).secondaryBackground,
                          child: ExpandableNotifier(
                            initialExpanded: false,
                            child: ExpandablePanel(
                              header: Padding(
                                padding:
                                    EdgeInsetsDirectional.fromSTEB(0, 60, 0, 0),
                                child: Text(
                                  widget.title,
                                  style: Theme.of(context)
                                      .headlineSmall
                                      .override(
                                        fontFamily: 'Rubik',
                                      ),
                                ),
                              ),
                              collapsed: Container(
                                width: MediaQuery.of(context).size.width,
                                height: 60,
                                decoration: BoxDecoration(
                                  color: Theme.of(context)
                                      .secondaryBackground,
                                ),
                                child: Padding(
                                  padding: EdgeInsetsDirectional.fromSTEB(
                                      0, 8, 0, 0),
                                  child: Text(
                                    widget.desc!,
                                    style: Theme.of(context)
                                        .labelMedium,
                                  ),
                                ),
                              ),
                              expanded: Column(
                                mainAxisSize: MainAxisSize.max,
                                children: [
                                  Padding(
                                    padding: EdgeInsetsDirectional.fromSTEB(
                                        0, 8, 0, 12),
                                    child: Text(
                                      'By protecting and preserving our oceans, we can effectively reduce global warming as healthy oceans absorb a significant amount of atmospheric carbon dioxide. Implementing measures to prevent overfishing, reducing plastic pollution, and conserving marine habitats will contribute to a balanced ocean ecosystem, ultimately mitigating global warming.',
                                      style: Theme.of(context)
                                          .labelMedium,
                                    ),
                                  ),
                                ],
                              ),
                              theme: ExpandableThemeData(
                                tapHeaderToExpand: true,
                                tapBodyToExpand: true,
                                tapBodyToCollapse: true,
                                headerAlignment:
                                    ExpandablePanelHeaderAlignment.center,
                                hasIcon: false,
                              ),
                            ),
                          ),
                        ),
                      ),
                    ],
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
