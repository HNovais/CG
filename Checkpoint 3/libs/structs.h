#ifndef CG_STRUCTS_H
#define CG_STRUCTS_H

#include <vector>
#include <string>

using namespace std;

struct Window {
    int width;
    int height;
};

struct Coords {
    float x;
    float y;
    float z;
};

struct Projection {
    float fov;
    float near;
    float far;
};

struct Camera {
    Coords position;
    Coords lookAt;
    Coords up;
    Projection projection;
};

struct Transform {
    string type;
    float x;
    float y;
    float z;
    float angle;

    float time;
    bool align;
    vector<float> movement;
    float transformMatrix[16];
};

struct Model {
    vector<float> colour;
    vector<float> points;
    string name;
};

struct Group {
    vector<Transform> transforms;
    vector<Model> models;
    vector<Group> groups;
};

struct Shortcut{
    bool line;
    bool axis;
};

struct XML_Struct {
    Window window;
    Camera camera;
    Group group;
    Shortcut shortcut;
};

#endif

