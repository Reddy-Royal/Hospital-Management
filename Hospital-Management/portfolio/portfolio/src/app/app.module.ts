import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { HeaderComponent } from './header/header.component';
import { HeroComponent } from './hero/hero.component';
import { AboutComponent } from './about/about.component';
import { EducationComponent } from './education/education.component';
import { ProjectsComponent } from './projects/projects.component';
import { SkillsComponent } from './skills/skills.component';
import { InternshipsComponent } from './internships/internships.component';
import { CertificationsComponent } from './certifications/certifications.component';
import { AchievementsComponent } from './achievements/achievements.component';
import { ContactComponent } from './contact/contact.component';
import { FooterComponent } from './footer/footer.component';
@NgModule({
    imports: [
      BrowserModule,
      AppComponent // Import the AppComponent directly if it's standalone
    ],
    bootstrap: [AppComponent]
  })
  export class AppModule { }
  