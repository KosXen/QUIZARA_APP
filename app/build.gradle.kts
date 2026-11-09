plugins {
    id("com.android.application")
}

android {
    namespace = "com.monomaxia.gnoseon"
    compileSdk = 36

    defaultConfig {
        applicationId = "com.monomaxia.gnoseon"
        minSdk = 23
        targetSdk = 36
        versionCode = 23
        versionName = "0.10.5"
    }

    buildTypes {
        release {
            isMinifyEnabled = false
        }
    }
}
