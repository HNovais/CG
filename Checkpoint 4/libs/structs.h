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
};

struct Color {
    string type;
    Coords values;
    int value;
};

struct Model {
    string name;
    string texture;
    unsigned int textureID;
    vector<float> colour;
    
    vector<float> points;
    vector<float> normals;
    vector<float> texcoords;

    vector<Color> color;
};

struct Group {
    vector<Transform> transforms;
    vector<Model> models;
    vector<Group> groups;
};

struct Lights {
    string type;
    Coords pos;
    Coords dir;
    int cutoff;
};

struct Shortcut{
    bool line = false;
    bool axis = true;
    bool catmull = true;
};

struct XML_Struct {
    Window window;
    Camera camera;
    Group group;
    Shortcut shortcut;
    vector<Lights> lights;
};

#endif

