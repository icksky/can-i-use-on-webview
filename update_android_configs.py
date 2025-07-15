#!/usr/bin/env python3
import os
import re

def update_gradle_wrapper_properties(file_path):
    """更新 gradle-wrapper.properties 文件"""
    with open(file_path, 'r') as f:
        content = f.read()
    
    # 更新 Gradle 版本到 7.6
    content = re.sub(
        r'distributionUrl=https\\://services\.gradle\.org/distributions/gradle-7\.0\.2-bin\.zip',
        'distributionUrl=https\\://services.gradle.org/distributions/gradle-7.6-bin.zip',
        content
    )
    
    with open(file_path, 'w') as f:
        f.write(content)
    
    print(f"已更新: {file_path}")

def update_build_gradle(file_path):
    """更新 build.gradle 文件"""
    with open(file_path, 'r') as f:
        content = f.read()
    
    # 更新 Android Gradle Plugin 版本
    content = re.sub(
        r'classpath "com\.android\.tools\.build:gradle:7\.0\.3"',
        'classpath "com.android.tools.build:gradle:7.4.2"',
        content
    )
    
    with open(file_path, 'w') as f:
        f.write(content)
    
    print(f"已更新: {file_path}")

def update_app_build_gradle(file_path):
    """更新 app/build.gradle 文件"""
    with open(file_path, 'r') as f:
        content = f.read()
    
    # 更新 compileSdk 和 targetSdk
    content = re.sub(r'compileSdk 31', 'compileSdk 33', content)
    content = re.sub(r'targetSdk 31', 'targetSdk 33', content)
    
    # 更新 Java 版本
    content = re.sub(r'JavaVersion\.VERSION_1_8', 'JavaVersion.VERSION_11', content)
    
    # 更新依赖版本
    content = re.sub(r"'androidx\.appcompat:appcompat:1\.3\.1'", "'androidx.appcompat:appcompat:1.6.1'", content)
    content = re.sub(r"'com\.google\.android\.material:material:1\.4\.0'", "'com.google.android.material:material:1.8.0'", content)
    content = re.sub(r"'androidx\.constraintlayout:constraintlayout:2\.0\.4'", "'androidx.constraintlayout:constraintlayout:2.1.4'", content)
    content = re.sub(r"'androidx\.webkit:webkit:1\.4\.0'", "'androidx.webkit:webkit:1.6.1'", content)
    content = re.sub(r"testImplementation 'junit:junit:4\.\+'", "testImplementation 'junit:junit:4.13.2'", content)
    content = re.sub(r"'androidx\.test\.ext:junit:1\.1\.3'", "'androidx.test.ext:junit:1.1.5'", content)
    content = re.sub(r"'androidx\.test\.espresso:espresso-core:3\.4\.0'", "'androidx.test.espresso:espresso-core:3.5.1'", content)
    
    with open(file_path, 'w') as f:
        f.write(content)
    
    print(f"已更新: {file_path}")

def main():
    """主函数"""
    android_projects = [
        'clipboard/android',
        'geolocation/android', 
        'getusermedia/android',
        'permissions/android',
        'share/android',
        'template/android'
    ]
    
    for project in android_projects:
        if os.path.exists(project):
            print(f"\n处理项目: {project}")
            
            # 更新 gradle-wrapper.properties
            wrapper_props = os.path.join(project, 'gradle', 'wrapper', 'gradle-wrapper.properties')
            if os.path.exists(wrapper_props):
                update_gradle_wrapper_properties(wrapper_props)
            
            # 更新 build.gradle
            build_gradle = os.path.join(project, 'build.gradle')
            if os.path.exists(build_gradle):
                update_build_gradle(build_gradle)
            
            # 更新 app/build.gradle
            app_build_gradle = os.path.join(project, 'app', 'build.gradle')
            if os.path.exists(app_build_gradle):
                update_app_build_gradle(app_build_gradle)

if __name__ == "__main__":
    main() 