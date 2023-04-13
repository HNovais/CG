#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <iostream>
#include <string>
#include <io.h>
#include <direct.h>
#include <structs.h>

#ifdef __APPLE__
#include <GLUT/glut.h>
#else
#include <GL/glut.h>
#endif

#include "rapidxml.hpp"
#include "rapidxml_utils.hpp"
#include "rapidxml_print.hpp"


using namespace rapidxml;
using namespace std;

XML_Struct estrutura;

float alpha = 0.0f;
float beta = 0.0f;
float offsetZ = 0.0f;
float offsetX = 0.0f;

float dx = 0, dy = 0, dz = 0;

void changeSize(int w, int h) {

	// Prevent a divide by zero, when window is too short
	// (you cant make a window with zero width).
	if(h == 0)
		h = 1;

	// compute window's aspect ratio 
	float ratio = w * 1.0 / h;

	// Set the projection matrix as current
	glMatrixMode(GL_PROJECTION);
	// Load Identity Matrix
	glLoadIdentity();
	
	// Set the viewport to be the entire window
	glViewport(0, 0, w, h);

	//gluPerspective(estrutura.camera.projection.fov, estrutura.window.width / estrutura.window.height, estrutura.camera.projection.near, estrutura.camera.projection.far);
	gluPerspective(45, ratio, 1, 1000);
	// return to the model view matrix mode
	glMatrixMode(GL_MODELVIEW);
}


void drawShape(Model model) {
	vector<float> coords = model.points;
	if (estrutura.shortcut.line==true){ glPolygonMode(GL_FRONT_AND_BACK, GL_LINE); }
	else { glPolygonMode(GL_FRONT_AND_BACK, GL_FILL); }

	if (model.colour.size() > 0)
		glColor3f(model.colour[0], model.colour[1], model.colour[2]);

	glBegin(GL_TRIANGLES);
	for (int j = 0; j < coords.size(); j += 9) {
		glVertex3f(coords[j], coords[j + 1], coords[j + 2]);
		glVertex3f(coords[j + 3], coords[j + 4], coords[j + 5]);
		glVertex3f(coords[j + 6], coords[j + 7], coords[j + 8]);
	}
	glEnd();
}


void transformation(Transform transform) {
	if (transform.type=="translate"){
		glTranslatef(transform.x, transform.y, transform.z);
	}
	else if (transform.type == "rotate") {
		glRotatef(transform.angle,transform.x, transform.y, transform.z);
	}
	else if (transform.type == "scale") {
		glScalef(transform.x, transform.y, transform.z);
	}
}


void processgroup(Group group) {
	glPushMatrix();

	for (int i = 0; i < group.transforms.size(); i++) {
		transformation(group.transforms[i]);
	}

	for (int i = 0; i < group.models.size(); i++) {
		drawShape(group.models[i]);
	}

	for (int i = 0; i < group.groups.size(); i++) {
		processgroup(group.groups[i]);
	}

	glPopMatrix();
}


void renderScene() {

	// clear buffers
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

	// set the camera
	glLoadIdentity();
	
	float camX = cos(beta) * sin(alpha);
	float camZ = cos(beta) * cos(alpha);

	gluLookAt(estrutura.camera.position.x , estrutura.camera.position.y, estrutura.camera.position.z,
		estrutura.camera.lookAt.x, estrutura.camera.lookAt.y, estrutura.camera.lookAt.z,
		estrutura.camera.up.x, estrutura.camera.up.y, estrutura.camera.up.z);

	if (estrutura.shortcut.axis != true) {
		glBegin(GL_LINES);
		// X axis in red
		glColor3f(1.0f, 0.0f, 0.0f);
		glVertex3f(
			-100.0f, 0.0f, 0.0f);
		glVertex3f(100.0f, 0.0f, 0.0f);
		// Y Axis in Green
		glColor3f(0.0f, 1.0f, 0.0f);
		glVertex3f(0.0f,
			-100.0f, 0.0f);
		glVertex3f(0.0f, 100.0f, 0.0f);
		// Z Axis in Blue
		glColor3f(0.0f, 0.0f, 1.0f);
		glVertex3f(0.0f, 0.0f,
			-100.0f);
		glVertex3f(0.0f, 0.0f, 100.0f);
		glEnd();
	}

	glColor3f(1.0f, 1.0f, 1.0f);

	processgroup(estrutura.group);
	
	// End of frame
	glutSwapBuffers();
}

void processKeys(unsigned char key, int xx, int yy) {
	dx = estrutura.camera.lookAt.x - estrutura.camera.position.x;
	dy = 0;
	dz = estrutura.camera.lookAt.z - estrutura.camera.position.z;

	float rx = -(dz * 1);
	float ry = 0;
	float rz = dx * 1;

	switch (key) {

	case 'w':
		estrutura.camera.position.x = estrutura.camera.position.x + dx;
		estrutura.camera.position.z = estrutura.camera.position.z + dz;
		break;

	case 'a':
		estrutura.camera.position.x -= rx;
		estrutura.camera.position.z -= rz;
		break;

	case 's':
		estrutura.camera.position.x = estrutura.camera.position.x - dx;
		estrutura.camera.position.z = estrutura.camera.position.z - dz;
		break;

	case 'd':
		estrutura.camera.position.x += rx;
		estrutura.camera.position.z += rz;
		break;

	case 'q':
		alpha += 0.1;
		break;

	case 'e':
		alpha -= 0.1;
		break;
	case 'l':
		if (estrutura.shortcut.line == true)estrutura.shortcut.line = false;
		else estrutura.shortcut.line = true;
		break;
	case 'k':
		if (estrutura.shortcut.axis == true)estrutura.shortcut.axis = false;
		else estrutura.shortcut.axis = true;
		break;
	}
	//camY = 1 + hf(camX + th / 2, camZ + tw / 2);

	estrutura.camera.lookAt.x = estrutura.camera.position.x + sin(alpha);
	estrutura.camera.lookAt.z = estrutura.camera.position.z + cos(alpha);
	estrutura.camera.lookAt.y = estrutura.camera.position.y;
	/*
	switch (key) {
	case 'q':
	case 'Q':
		alpha += 0.1f;
		break;
	case 'e':
	case 'E':
		alpha -= 0.1f;
		break;
	case 'w':
	case 'W':
		offsetZ += 1.0f;
		break;
	case 's':
	case 'S':
		offsetZ -= 1.0f;
		break;
	case 'd':
	case 'D':
		offsetX += 1.0f;
		break;
	case 'a':
	case 'A':
		offsetX -= 1.0f;
		break;
	case 'l':
		if (estrutura.shortcut.line == true)estrutura.shortcut.line = false;
		else estrutura.shortcut.line = true;
	default:
		break;
	}
	*/
	glutPostRedisplay();
}

void processSpecialKeys(int key, int xx, int yy) {
	
	switch (key) {
	case GLUT_KEY_UP:
		estrutura.camera.position.y = estrutura.camera.position.y + 1;
		break;

	case GLUT_KEY_DOWN:
		estrutura.camera.position.y = estrutura.camera.position.y - 1;
		break;

	}
	estrutura.camera.lookAt.y = estrutura.camera.position.y;
	
	glutPostRedisplay();

}

Group readGroup(Group group, xml_node<>* groupNode) {
	xml_node<>* transformNode = groupNode->first_node("transform");
	xml_node<>* modelsNode = groupNode->first_node("models");
	xml_node<>* groupsNode = groupNode->first_node("group");

	if (transformNode != NULL) {
		bool t = false, r = false, s = false;
		
		for (xml_node<>* childNode = transformNode->first_node(); childNode != NULL; childNode = childNode->next_sibling()) {
			string nodeName = childNode->name();

			if (nodeName == "translate" && !t) {
				Transform translate;

				translate.type = "translate";
				translate.x = stof(childNode->first_attribute("x")->value());
				translate.y = stof(childNode->first_attribute("y")->value());
				translate.z = stof(childNode->first_attribute("z")->value());

				printf("Tranlation: X: %.1f  Y: %.1f  Z: %.1f\n", translate.x, translate.y, translate.z);

				group.transforms.push_back(translate);
				t = true;
			}

			if (nodeName == "rotate" && !r) {
				Transform rotate;

				rotate.type = "rotate";
				rotate.angle = stof(childNode->first_attribute("angle")->value());
				rotate.x = stof(childNode->first_attribute("x")->value());
				rotate.y = stof(childNode->first_attribute("y")->value());
				rotate.z = stof(childNode->first_attribute("z")->value());

				printf("Rotation: Angle: %.1f X: %.1f  Y: %.1f  Z: %.1f\n", rotate.angle, rotate.x, rotate.y, rotate.z);

				group.transforms.push_back(rotate);
				r = true;
			}

			if (nodeName == "scale" && !s) {
				Transform scale;

				scale.type = "scale";
				scale.x = stof(childNode->first_attribute("x")->value());
				scale.y = stof(childNode->first_attribute("y")->value());
				scale.z = stof(childNode->first_attribute("z")->value());

				printf("Scale: X: %.1f  Y: %.1f  Z: %.1f\n", scale.x, scale.y, scale.z);

				group.transforms.push_back(scale);
				s = true;
			}
		}
	}

	if (modelsNode != NULL) {
		xml_node<>* colourNode = modelsNode->first_node("colour");


		xml_node<>* modelNode = modelsNode->first_node("model");

		while (modelNode != NULL)
		{
			char cwd[1024];

			string file = modelNode->first_attribute("file")->value();

			Model model;

			float x, y, z;
			string file_path = "../src/" + file;
			cout << "Loading model from file: " << file_path << "\n" << std::endl;

			ifstream infile(file_path);

			while (infile >> x >> y >> z) {
				model.points.push_back(x);
				model.points.push_back(y);
				model.points.push_back(z);
			}

			if (colourNode != NULL) {
				x = stof(colourNode->first_attribute("r")->value());
				y = stof(colourNode->first_attribute("g")->value());
				z = stof(colourNode->first_attribute("b")->value());

				model.colour.push_back(x);
				model.colour.push_back(y);
				model.colour.push_back(z);
			}

			group.models.push_back(model);
			
			modelNode = modelNode->next_sibling("model");
		}
	}

	if (groupsNode != NULL) {
		while (groupsNode != NULL) {
			Group newGroup;
			group.groups.push_back(readGroup(newGroup, groupsNode));
			groupsNode = groupsNode->next_sibling("group");
		}
	}

	return group;
}


void loadXML(XML_Struct& estrutura) {

	// Load the XML file
	file<> xmlFile("../src/configuration.xml");

	// Parse the XML file
	xml_document<> doc;
	doc.parse<0>(xmlFile.data());

	// Get the root node
	xml_node<>* rootNode = doc.first_node("world");

	// Get the window node and its attributes
	xml_node<>* windowNode = rootNode->first_node("window");
	estrutura.window.width= stoi(windowNode->first_attribute("width")->value());
	estrutura.window.height = stoi(windowNode->first_attribute("height")->value());

	// Get the camera node and its children
	xml_node<>* cameraNode = rootNode->first_node("camera");
	xml_node<>* positionNode = cameraNode->first_node("position");
	xml_node<>* lookAtNode = cameraNode->first_node("lookAt");
	xml_node<>* upNode = cameraNode->first_node("up");
	xml_node<>* projectionNode = cameraNode->first_node("projection");

	std::cout << "Camera Values: " << "X: " << std::stof(positionNode->first_attribute("x")->value()) << " Y: " << std::stof(positionNode->first_attribute("y")->value()) << " Z: " << std::stof(positionNode->first_attribute("z")->value()) << std::endl;
	estrutura.camera.position.x = stof(positionNode->first_attribute("x")->value());
	estrutura.camera.position.y = stof(positionNode->first_attribute("y")->value());
	estrutura.camera.position.z = stof(positionNode->first_attribute("z")->value());

	estrutura.camera.lookAt.x = stof(lookAtNode->first_attribute("x")->value());
	estrutura.camera.lookAt.y = stof(lookAtNode->first_attribute("y")->value());
	estrutura.camera.lookAt.z = stof(lookAtNode->first_attribute("z")->value());
	printf("Look At: X: %.1f  Y: %.1f  Z: %.1f\n", estrutura.camera.lookAt.x, estrutura.camera.lookAt.y, estrutura.camera.lookAt.z);

	estrutura.camera.up.x = stof(upNode->first_attribute("x")->value());
	estrutura.camera.up.y = stof(upNode->first_attribute("y")->value());
	estrutura.camera.up.z = stof(upNode->first_attribute("z")->value());
	printf("Up: X: %.1f  Y: %.1f  Z: %.1f\n", estrutura.camera.up.x, estrutura.camera.up.y, estrutura.camera.up.z);

	estrutura.camera.projection.far= stof(projectionNode->first_attribute("far")->value());;
	estrutura.camera.projection.fov= stof(projectionNode->first_attribute("fov")->value());;
	estrutura.camera.projection.near=stof(projectionNode->first_attribute("near")->value());
	printf("Projection: FOV: %.1f  near: %.1f  far: %.1f\n\n", estrutura.camera.projection.fov, estrutura.camera.projection.near, estrutura.camera.projection.far);

	// Get the group node and its child nodes

	xml_node<>* groupNode = rootNode->first_node("group");

	if (groupNode != NULL) 
		estrutura.group = readGroup(estrutura.group, groupNode);
}


int main(int argc, char **argv) {

	loadXML(estrutura);

// init GLUT and the window
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_DEPTH|GLUT_DOUBLE|GLUT_RGBA);
	glutInitWindowPosition(100,100);
	glutInitWindowSize(estrutura.window.width, estrutura.window.height);
	glutCreateWindow("grupo31");
		
// Required callback registry 
	glutDisplayFunc(renderScene);
	glutReshapeFunc(changeSize);
	
// Callback registration for keyboard processing
	glutKeyboardFunc(processKeys);
	glutSpecialFunc(processSpecialKeys);
//  OpenGL settings
	glEnable(GL_DEPTH_TEST);
	glEnable(GL_CULL_FACE);
	
// enter GLUT's main cycle
	glutMainLoop();
	
	return 1;
}
